# Generated by Django 3.2.5 on 2021-07-22 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ep3', '0018_amostra_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amostra',
            name='exame',
        ),
        migrations.RemoveField(
            model_name='amostra',
            name='paciente',
        ),
    ]
