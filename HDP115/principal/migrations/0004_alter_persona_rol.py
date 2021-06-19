# Generated by Django 3.2.3 on 2021-06-19 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_alter_entregapaquete_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='rol',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)]),
        ),
    ]