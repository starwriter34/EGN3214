# Generated by Django 3.0.7 on 2020-09-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinestatus',
            name='downtime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='machinestatus',
            name='machine_row',
            field=models.CharField(choices=[('A', 'A Row'), ('B', 'B Row'), ('C', 'C Row'), ('D', 'D Row'), ('E', 'E Row'), ('F', 'F Row'), ('G', 'G Row'), ('H', 'H Row'), ('I', 'I Row'), ('J', 'J Row'), ('K', 'K Row'), ('L', 'L Row'), ('M', 'M Row'), ('N', 'N Row'), ('O', 'O Row'), ('P', 'P Row'), ('Q', 'Q Row'), ('R', 'R Row'), ('S', 'S Row'), ('T', 'T Row'), ('U', 'U Row'), ('V', 'V Row'), ('W', 'W Row'), ('X', 'X Row'), ('Y', 'Y Row'), ('Z', 'Z Row')], max_length=1, verbose_name='Machine Row'),
        ),
        migrations.AlterField(
            model_name='machinestatus',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
    ]
