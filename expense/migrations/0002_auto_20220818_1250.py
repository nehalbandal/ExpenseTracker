# Generated by Django 3.2 on 2022-08-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmoneycollection',
            name='building',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('B1', 'B1'), ('B2', 'B2'), ('OTHERS', 'Others')], default='OTHERS', max_length=300),
        ),
        migrations.AddField(
            model_name='historicalmoneycollection',
            name='flat_no',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalmoneycollection',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid')], default='PENDING', max_length=300),
        ),
        migrations.AddField(
            model_name='moneycollection',
            name='building',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('B1', 'B1'), ('B2', 'B2'), ('OTHERS', 'Others')], default='OTHERS', max_length=300),
        ),
        migrations.AddField(
            model_name='moneycollection',
            name='flat_no',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='moneycollection',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid')], default='PENDING', max_length=300),
        ),
    ]
