# Generated by Django 3.2.5 on 2021-07-22 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep3', '0014_alter_agregado_paciente_exame_amostra_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='exame',
            name='amostra',
            field=models.ManyToManyField(through='ep3.Agregado_Paciente_Exame_Amostra', to='ep3.Amostra'),
        ),
    ]
