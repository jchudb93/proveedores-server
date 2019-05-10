# Generated by Django 2.2.1 on 2019-05-10 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateStart', models.CharField(max_length=10)),
                ('dateEnd', models.CharField(max_length=10)),
                ('state', models.CharField(choices=[('Activo', 'Activo'), ('Calificado', 'Calificado'), ('Finalizado', 'Finalizado')], default='Activo', max_length=12)),
                ('percentage', models.FloatField()),
                ('contract_file', models.CharField(max_length=200)),
                ('in_charge_points', models.IntegerField(blank=True)),
                ('quality_points', models.IntegerField(blank=True)),
                ('contract_points', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrategicGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=12)),
                ('cell', models.CharField(max_length=12)),
                ('ruc', models.IntegerField()),
                ('state', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('dateLimit', models.CharField(max_length=10)),
                ('dateEnd', models.CharField(max_length=10)),
                ('notification', models.BooleanField()),
                ('done', models.BooleanField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Contract')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('service_category', models.CharField(max_length=255)),
                ('strategic_goals', models.ManyToManyField(blank=True, to='providers.StrategicGoal')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=12)),
                ('cell', models.CharField(max_length=12)),
                ('web', models.CharField(max_length=255)),
                ('ruc', models.IntegerField()),
                ('state', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('provider_type', models.CharField(choices=[('Externo', 'Externo'), ('Interno', 'Interno')], default='Externo', max_length=7)),
                ('category', models.CharField(choices=[('Estratégico', 'Estratégico'), ('Operativo', 'Operativo'), ('Táctico', 'Táctico'), ('Básico', 'Básico')], default='Básico', max_length=12)),
                ('suppliers', models.ManyToManyField(blank=True, to='providers.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('fulfillment', models.BooleanField()),
                ('satisfaction', models.FloatField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Contract')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.Provider'),
        ),
        migrations.AddField(
            model_name='contract',
            name='services',
            field=models.ManyToManyField(blank=True, to='providers.Service'),
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('minimum', models.CharField(max_length=255)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Contract')),
            ],
        ),
    ]