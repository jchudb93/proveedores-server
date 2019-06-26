# Generated by Django 2.2.1 on 2019-06-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0016_auto_20190623_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='dateEnd',
            field=models.DateField(blank=True, null=True, verbose_name=('%d/%m/%Y', '%Y/%m/%d')),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dateStart',
            field=models.DateField(blank=True, null=True, verbose_name=('%d/%m/%Y', '%Y/%m/%d')),
        ),
        migrations.AlterField(
            model_name='task',
            name='dateEnd',
            field=models.DateField(blank=True, null=True, verbose_name=('%d/%m/%Y', '%Y/%m/%d')),
        ),
        migrations.AlterField(
            model_name='task',
            name='dateLimit',
            field=models.DateField(blank=True, null=True, verbose_name=('%d/%m/%Y', '%Y/%m/%d')),
        ),
    ]