# Generated by Django 3.2.5 on 2021-07-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep3', '0024_auto_20210723_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exame',
            name='paciente',
        ),
        migrations.AddField(
            model_name='exame',
            name='paciente',
            field=models.ManyToManyField(through='ep3.Agregado_Paciente_Exame_Amostra', to='ep3.Paciente'),
        ),
    ]
