# Generated by Django 3.0.7 on 2020-10-15 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmaint', '0013_auto_20201015_0944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machinestatus',
            options={'ordering': ['status', 'machine_name'], 'permissions': [('pso_indicating_fixture', "PSO's Indicating the fixture status"), ('pm_preventative_maintenance', 'Can put machine into preventative maintenance status'), ('machine_down_supervisor', 'Only has access to put machine up or down'), ('mmaint_all', 'Will see all buttons for Machine Status')], 'verbose_name': 'Machine Status', 'verbose_name_plural': 'Machine Status'},
        ),
    ]
