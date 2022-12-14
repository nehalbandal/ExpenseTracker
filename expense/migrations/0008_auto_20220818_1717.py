# Generated by Django 3.2 on 2022-08-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0007_auto_20220818_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='attachment',
            field=models.FileField(blank=True, max_length=255, upload_to='expenses/%Y/%M/%D/', verbose_name='Attachment Path'),
        ),
        migrations.AlterField(
            model_name='moneycollection',
            name='attachment',
            field=models.FileField(blank=True, max_length=255, upload_to='collection/%Y/%M/%D/', verbose_name='Attachment'),
        ),
    ]
