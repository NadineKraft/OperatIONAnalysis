# Generated by Django 3.1.7 on 2021-03-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_experimentmodel_config_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='configmodel',
            name='guppy_params',
            field=models.CharField(default='', max_length=255),
        ),
    ]