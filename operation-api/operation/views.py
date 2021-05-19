from rest_framework import generics
from rest_framework.response import Response

from .models import ExperimentModel
from .models import ConfigModel
from .models import AnalysisModel
from .serializers import ExperimentSerializer
from .serializers import AnalysisSerializer

from .serializers import ConfigSerializer

from .operation_analysis.analysis.Analysis import Analysis
from .operation_analysis.analysis.PycoQC import PycoQC
from .operation_analysis.analysis.NanoGladiatorCNVSource import NanoGladiatorCNVSource

from .operation_analysis.processing.Processing import Processing
from .operation_analysis.processing.MegalodonProcessor import MegalodonProcessor
from .operation_analysis.processing.MegalodonSource import MegalodonSource

from .operation_analysis.directory_management.SaveConfig import saveConfigFile

import threading
import time


class ConfigList(generics.ListCreateAPIView):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigSerializer


class ConfigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigSerializer


    def get_queryset(self):
        data = ConfigModel.objects.all()
        return data

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        #current = self.get_serializer(instance).data

        self.perform_update(serializer)
        result = serializer.data
        return Response(result)


class ExperimentList(generics.ListCreateAPIView):
    queryset = ExperimentModel.objects.all()
    serializer_class = ExperimentSerializer


class ExperimentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExperimentModel.objects.all()
    serializer_class = ExperimentSerializer

    def get_queryset(self):
        data = ExperimentModel.objects.all()
        return data

    def update(self, request, *args, **kwargs):
        global t1
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        current = self.get_serializer(instance).data

        self.perform_update(serializer)
        result = serializer.data

        # experiment = ExperimentModel.objects.get(pk=current["id"])

        if current['processed'] == 'INITIATED' and result['processed'] == 'PENDING':
            t1 = threading.Thread(target=run_processing, args=[current["id"]])
            t1.setDaemon(True)
            t1.start()

        # TODO: Fehler abfangen
        elif current['processed'] == 'COMPLETED':
            experiment = ExperimentModel.objects.get(pk=current["id"])
            experiment.processed = "ERROR"
            experiment.save()

        return Response(result)


def run_processing(experiment_id):
    experiment = ExperimentModel.objects.get(pk=experiment_id)
    experiment_data = ExperimentSerializer(experiment).data
    config = ConfigModel.objects.get(pk=experiment.config_id)
    config_data = ConfigSerializer(config).data

    processor = MegalodonProcessor(MegalodonSource(experiment, config))
    Processing(processor).perform()

    #saveConfigFile(config_data, experiment_data)
    experiment.processed = "COMPLETED"
    experiment.save()


class AnalysisList(generics.ListCreateAPIView):
    queryset = AnalysisModel.objects.all()
    serializer_class = AnalysisSerializer


class AnalysisDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnalysisSerializer
    lookup_field = "pk"

    def get_queryset(self):
        data = AnalysisModel.objects.all()
        return data

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        current = self.get_serializer(instance).data

        self.perform_update(serializer)
        result = serializer.data

        if current['status'] == 'INITIATED' and result['status'] == 'PENDING':
            t2 = threading.Thread(target=run_analysis, args=[current["id"]])
            t2.setDaemon(True)
            t2.start()
            time.sleep(200)
            # Rerun analysis if processing has not finished
            while t1.is_alive():
                t2 = threading.Thread(target=run_analysis, args=[current["id"]])
                t2.setDaemon(True)
                t2.start()
                time.sleep(300)
            print("Done!")

        else:
            analysis = AnalysisModel.objects.get(pk=current["id"])
            analysis.status = "ERROR"
            analysis.save()

        return Response(result)


# @background(schedule=1)
def run_analysis(analysis_id):
    analysis = AnalysisModel.objects.get(pk=analysis_id)
    experiment = ExperimentModel.objects.get(pk=analysis.experiment_id)
    config = ConfigModel.objects.get(pk=experiment.config_id)

    analysis_methylation_analysis = analysis.methylation_analysis
    analysis_status_parameter = analysis.status_parameter_analysis
    analysis_copy_number_variation = analysis.copy_number_variation_analysis
    Analyser = []
    if analysis_status_parameter:
        print('analysis status parameter')
        # TODO: Modify Path
        status_parameter_output_directory = '/home/nadine/vue_projects/crud-vuejs-django-rest-framework' \
                                            '/operation' \
                                            '-app/public/results/'
        status_parameter_source = PycoQC(config.status_parameter_input_directory,
                                         status_parameter_output_directory, analysis.prefix)
        Analyser.append(status_parameter_source)
    if analysis_methylation_analysis:
        print('analysis methylation')
    if analysis_copy_number_variation:
        print('analysis copy_number_variation')
        cnv_chromosome_list = [
            'chr1,chr2,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chr10,chr11,chr12,chr13,chr14,chr15,chr16,'
            'chr17,chr18,chr19,chr20,chr21,chr22,chr23,chr24']
        cnv_output_directory = '/home/nadine/vue_projects/crud-vuejs-django-rest-framework/operation' \
                               '-app/public/results/'
        copy_number_variation_source = NanoGladiatorCNVSource(analysis.prefix, cnv_chromosome_list,
                                                              config.cnv_input_directory,
                                                              cnv_output_directory)
        Analyser.append(copy_number_variation_source)

    if not Analyser:
        analysis.status = "FAILED"
        analysis.save()

    else:
        Analysis(Analyser).analyse()
        analysis.status = "COMPLETED"
        analysis.save()
