# Generated by Django 2.2.1 on 2019-06-10 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0005_auto_20190610_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.Contract'),
        ),
        migrations.AlterField(
            model_name='task',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.Contract'),
        ),
    ]
