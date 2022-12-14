# Generated by Django 4.1 on 2022-08-16 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('name', models.CharField(max_length=300)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='money_added', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='money_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Money Collection',
                'verbose_name_plural': 'Money Collection',
            },
        ),
        migrations.CreateModel(
            name='HistoricalMoneyCollection',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('modification_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modification Date')),
                ('creation_date', models.DateTimeField(blank=True, editable=False, verbose_name='Creation Date')),
                ('name', models.CharField(max_length=300)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('added_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Money Collection',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalExpense',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('modification_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modification Date')),
                ('creation_date', models.DateTimeField(blank=True, editable=False, verbose_name='Creation Date')),
                ('expense_name', models.CharField(max_length=300)),
                ('expense_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('expense_owner', models.CharField(max_length=300)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('added_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Expense',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('expense_name', models.CharField(max_length=300)),
                ('expense_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('expense_owner', models.CharField(max_length=300)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expense_added', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expense_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
    ]
