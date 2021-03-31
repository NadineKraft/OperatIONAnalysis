from rest_framework import serializers
from .models import ExperimentModel
from .models import ConfigModel
from .models import AnalysisModel


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigModel
        fields = ('id', 'name', 'basecaller', 'megalodon_input_directory', 'megalodon_output_directory',
                  'fasta_reference_directory', 'guppy_config', 'guppy_server_path',
                  'guppy_params', 'megalodon_devices', 'megalodon_processes',
                  'methylationcaller', 'aligner', 'status_parameter_input_directory',
                  'status_parameter_output_directory', 'cnv_input_directory', 'created_at', 'updated_at')


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentModel
        fields = ('id', 'name', 'description', 'live_processing',
                  'basecalling', 'methylation_calling', 'alignment', 'fast5_dir', 'processed', 'config_id',
                  'created_at', 'updated_at')


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisModel
        fields = ('id', 'name', 'status', 'methylation_analysis', 'copy_number_variation_analysis', 'prefix',
                  'status_parameter_analysis', 'experiment_id', 'created_at', 'updated_at')
