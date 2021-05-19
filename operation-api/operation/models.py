from django.db import models
from enum import Enum


# Create your models here.
class ConfigModel(models.Model):
    name = models.CharField(max_length=255, default="")
    basecaller = models.CharField(max_length=255, default="")
    megalodon_output_directory = models.CharField(max_length=255, default="")
    megalodon_parameters = models.CharField(max_length=255, default="")
    fasta_reference_directory = models.CharField(max_length=255, default="")
    guppy_config = models.CharField(max_length=255, default="")
    guppy_server_path = models.CharField(max_length=255, default="")
    guppy_params = models.CharField(max_length=255, default="")
    megalodon_devices = models.CharField(max_length=255, default="")
    megalodon_processes = models.CharField(max_length=255, default="")
    methylationcaller = models.CharField(max_length=255, default="")
    aligner = models.CharField(max_length=255, default="")
    status_parameter_input_directory = models.CharField(max_length=255, default="")
    status_parameter_output_directory = models.CharField(max_length=255, default="")
    cnv_input_directory = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
class ExperimentModel(models.Model):

    class TransactionStatus(Enum):
        INITIATED = "INITIATED"
        PENDING = "PENDING"
        COMPLETED = "COMPLETED"
        FAILED = "FAILED"
        ERROR = "ERROR"

        @classmethod
        def choices(cls):
            return tuple((i.name, i.value) for i in cls)

    name = models.CharField(max_length=255)
    live_processing = models.BooleanField(default=False)
    basecalling = models.BooleanField(default=False)
    methylation_calling = models.BooleanField(default=False)
    alignment = models.BooleanField(default=False)
    fast5_dir = models.CharField(max_length=255)
    processed = models.CharField(max_length=255, choices=TransactionStatus.choices())
    config_id = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AnalysisModel(models.Model):

    class TransactionStatus(Enum):
        INITIATED = "INITIATED"
        PENDING = "PENDING"
        COMPLETED = "COMPLETED"
        FAILED = "FAILED"
        ERROR = "ERROR"

        @classmethod
        def choices(cls):
            return tuple((i.name, i.value) for i in cls)

    name = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=255, choices=TransactionStatus.choices())
    methylation_analysis = models.BooleanField(default=False)
    copy_number_variation_analysis = models.BooleanField(default=False)
    prefix = models.CharField(max_length=255, default="")
    status_parameter_analysis = models.BooleanField(default=False)
    experiment_id = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

