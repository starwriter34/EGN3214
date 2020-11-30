# Generated by Django 3.0.7 on 2020-09-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmaint', '0003_auto_20200922_0619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machinestatus',
            options={'ordering': ['status', 'machine_name'], 'verbose_name': 'Machine Status', 'verbose_name_plural': 'Machine Status'},
        ),
        migrations.AlterField(
            model_name='machinestatus',
            name='status',
            field=models.CharField(choices=[('3', 'Running'), ('2', 'Waiting on Parts'), ('1', 'Down for Repair')], default='R', max_length=1, verbose_name='Machine Status'),
        ),
    ]