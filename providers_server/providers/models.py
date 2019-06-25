from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
# Create your models here.


class StrategicGoal(models.Model):

    name = models.CharField(max_length=255)
    

class Service(models.Model):
    name = models.CharField(max_length=255)
    service_category = models.CharField(max_length=255)
    strategic_goals = models.ManyToManyField(StrategicGoal, blank=True)

    def __str__(self):
        return self.name + " " + self.service_category


class Supplier(models.Model):
    ACTIVE = 'Activo'
    INACTIVE = 'Inactivo'
    STATE_CHOICES = (
        (ACTIVE, 'Activo'),
        (INACTIVE, 'Inactivo')
    )
    EXTERNAL = 'Externo'
    INTERNAL = 'Interno'
    TYPE_CHOICES = (
        (EXTERNAL, 'Externo'),
        (INTERNAL, 'Interno')
    )
    contact = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=12)
    cell = models.CharField(max_length=12)
    ruc = models.IntegerField(blank=False)
    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default=ACTIVE
    )


class Provider(models.Model):

    ACTIVE = 'Activo'
    INACTIVE = 'Inactivo'
    STATE_CHOICES = (
        (ACTIVE, 'Activo'),
        (INACTIVE, 'Inactivo')
    )
    EXTERNAL = 'Externo'
    INTERNAL = 'Interno'
    TYPE_CHOICES = (
        (EXTERNAL, 'Externo'),
        (INTERNAL, 'Interno')
    )

    STRATEGIC = 'Estratégico'
    OPERATIONAL = 'Operativo'
    TACTIC = 'Táctico'
    BASIC = 'Básico'

    CATEGORY_CHOICES = (
        (STRATEGIC, 'Estratégico'),
        (OPERATIONAL, 'Operativo'),
        (TACTIC, 'Táctico'),
        (BASIC, 'Básico')
    )

    contact = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=12)
    cell = models.CharField(max_length=12)
    web = models.CharField(max_length=255)
    ruc = models.IntegerField(blank=False)
    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default=ACTIVE
    )
    provider_type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES,
        default=EXTERNAL,
    )
    category = models.CharField(
        max_length=12,
        choices=CATEGORY_CHOICES,
        default=BASIC
    )
    suppliers = models.ManyToManyField(Supplier, blank=True)


class Contract(models.Model):

    ACTIVE = 'Activo'
    QUALIFIED = 'Calificado'
    FINISHED = 'Finalizado'
    STATE_CHOICES = (
        (ACTIVE, 'Activo'),
        (QUALIFIED, 'Calificado'),
        (FINISHED, 'Finalizado')
    )
    dateStart = models.DateField(
        settings.DATE_INPUT_FORMATS,
        null=True,
        blank=True)
    dateEnd = models.DateField(
        settings.DATE_INPUT_FORMATS,
        null=True,
        blank=True)
    state = models.CharField(
        max_length=12,
        choices=STATE_CHOICES,
        default=ACTIVE
    )

    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    percentage = models.FloatField(blank=True, null=True)
    contract_file = models.CharField(max_length=200)
    in_charge_points = models.IntegerField(blank=True,  null=True)
    quality_points = models.IntegerField(blank=True,  null=True)
    contract_points = models.IntegerField(blank=True,  null=True)
    services = models.ManyToManyField(Service, blank=True)
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name='contract_providers',
        null=True,
        blank=True
        )


class Agreement(models.Model):
    name = models.TextField()
    description = models.TextField()
    minimum = models.CharField(max_length=255)
    points = models.IntegerField(blank=True, null=True)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='agreement_contracts',
        null=True,
        blank=True)


class Incident(models.Model):
    description = models.TextField()
    fulfillment = models.BooleanField(blank=True, null=True)
    satisfaction = models.FloatField(blank=True, null=True)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='incident_contracts',
        null=True,
        blank=True)


class Task(models.Model):
    name = models.TextField()
    dateLimit = models.DateField(
        settings.DATE_INPUT_FORMATS,
        null=True,
        blank=True)
    dateEnd = models.DateField(
        settings.DATE_INPUT_FORMATS,
        null=True,
        blank=True)
    notification = models.BooleanField(null=True, blank=True)
    done = models.BooleanField(default=False)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='task_contracts',
        null=True,
        blank=True)
