# Generated by Django 3.0.7 on 2020-09-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmaint', '0005_machinestatus_downtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinestatus',
            name='downtime',
            field=models.DateTimeField(blank=True, help_text='If the machine is down enter Time and Date as shown: YYYY-MM-DD HH:MM:SS', null=True),
        ),
        migrations.AlterField(
            model_name='machinestatus',
            name='status',
            field=models.CharField(choices=[('3', 'Running'), ('2', 'Waiting on Parts'), ('1', 'Down for Repair')], default='3', max_length=1, verbose_name='Machine Status'),
        ),
    ]
