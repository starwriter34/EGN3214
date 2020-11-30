# Generated by Django 3.0.7 on 2020-09-29 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mmaint', '0009_auto_20200923_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineDownReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField(blank=True, null=True)),
                ('endtime', models.DateTimeField(blank=True, null=True)),
                ('machine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmaint.MachineStatus', verbose_name='Machine Number')),
            ],
        ),
    ]