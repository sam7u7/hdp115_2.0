# Generated by Django 3.2.4 on 2021-06-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_entregapaquete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregapaquete',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]