# Generated by Django 3.1.6 on 2021-12-05 22:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudio_socioeconomico', '0003_auto_20211205_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiosocioeconomico',
            name='numero_exterior',
            field=models.PositiveIntegerField(default=0, validators=[
                                              django.core.validators.MinValueValidator(1)], verbose_name='Número exterior'),
        ),
        migrations.AlterField(
            model_name='estudiosocioeconomico',
            name='numero_interior',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[
                                              django.core.validators.MinValueValidator(1)], verbose_name='Número interior'),
        ),
    ]
