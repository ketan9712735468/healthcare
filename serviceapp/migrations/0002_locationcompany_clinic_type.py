# Generated by Django 3.2.2 on 2021-05-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationcompany',
            name='clinic_type',
            field=models.CharField(choices=[('Spital', 'Spital'), ('Centru medical', 'Centru medical'), ('Centru diagnostic', 'Centru diagnostic'), ('Laborator', 'Laborator'), ('Stomatologie', 'Stomatologie'), ('Medicină estetică', 'Medicină estetică'), ('Clinică FIV', 'Clinică FIV')], default='Centru medical', max_length=20),
        ),
    ]
