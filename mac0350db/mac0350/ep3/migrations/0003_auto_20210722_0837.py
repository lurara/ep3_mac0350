# Generated by Django 3.2.5 on 2021-07-22 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ep3', '0002_auto_20210722_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregado_paciente_exame_amostra',
            name='amostra',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ep3.amostra'),
        ),
        migrations.AlterField(
            model_name='agregado_paciente_exame_amostra',
            name='exame',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ep3.exame'),
        ),
        migrations.AlterField(
            model_name='agregado_paciente_exame_amostra',
            name='paciente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ep3.paciente'),
        ),
    ]
