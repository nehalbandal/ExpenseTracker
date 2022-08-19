# Generated by Django 3.2 on 2022-08-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0010_alter_moneycollection_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='attachment',
            field=models.ImageField(blank=True, max_length=255, upload_to='expenses/%Y/%m/%d/', verbose_name='Attachment'),
        ),
        migrations.AlterField(
            model_name='historicalexpense',
            name='attachment',
            field=models.TextField(blank=True, max_length=255, verbose_name='Attachment'),
        ),
    ]