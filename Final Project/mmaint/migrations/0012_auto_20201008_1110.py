# Generated by Django 3.0.7 on 2020-10-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmaint', '0011_auto_20200929_1006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machinedownreports',
            options={'verbose_name': 'Machine Down Reports', 'verbose_name_plural': 'Machine Down Reports'},
        ),
        migrations.AlterField(
            model_name='machinestatus',
            name='notes',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='permanentrecords',
            name='reason',
            field=models.CharField(choices=[('1', 'General Note'), ('2', 'Crash'), ('3', 'Preventive Maintenance'), ('4', 'Repair'), ('5', 'Auto-Generated Note')], max_length=2, verbose_name='Reason for Record'),
        ),
    ]
