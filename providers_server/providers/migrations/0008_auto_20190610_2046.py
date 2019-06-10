# Generated by Django 2.2.1 on 2019-06-10 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0007_auto_20190610_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agreement_contracts', to='providers.Contract'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incident_contracts', to='providers.Contract'),
        ),
        migrations.AlterField(
            model_name='task',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_contracts', to='providers.Contract'),
        ),
    ]
