# Generated by Django 3.1.7 on 2021-03-18 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_remove_configmodel_cnv_output_directory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configmodel',
            name='megalodon_mod_motif',
        ),
    ]
