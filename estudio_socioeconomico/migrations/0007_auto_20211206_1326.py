# Generated by Django 3.1.6 on 2021-12-06 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudio_socioeconomico', '0006_auto_20211206_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiosocioeconomico',
            name='numero_banios',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Número de baños'),
        ),
        migrations.AlterField(
            model_name='estudiosocioeconomico',
            name='numero_recamaras',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Número de recamaras'),
        ),
    ]
