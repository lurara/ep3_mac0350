# Generated by Django 3.2.5 on 2021-07-22 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ep3', '0009_agregado_paciente_exame_amostra_data_de_solicitacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agregado_paciente_exame_amostra',
            name='data_de_realizacao',
        ),
    ]