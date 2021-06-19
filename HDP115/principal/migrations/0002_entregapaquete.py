# Generated by Django 3.2.4 on 2021-06-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='entregaPaquete',
            fields=[
                ('idEntrega', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.CharField(max_length=50)),
                ('dui', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(verbose_name=False)),
            ],
        ),
    ]
