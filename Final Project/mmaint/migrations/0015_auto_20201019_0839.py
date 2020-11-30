# Generated by Django 3.0.7 on 2020-10-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmaint', '0014_auto_20201015_1031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permanentrecords',
            options={'ordering': ['-date'], 'verbose_name': 'Repair Action Records', 'verbose_name_plural': 'Repair Actions Records'},
        ),
        migrations.AlterField(
            model_name='permanentrecords',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Note'),
        ),
    ]
