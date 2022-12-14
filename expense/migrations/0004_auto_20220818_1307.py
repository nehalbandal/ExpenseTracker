# Generated by Django 3.2 on 2022-08-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_auto_20220818_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmoneycollection',
            name='amount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='moneycollection',
            name='amount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
    ]
