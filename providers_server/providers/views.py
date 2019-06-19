from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *


# Create your views here.
class StrategicGoalView(viewsets.ModelViewSet):
    queryset = StrategicGoal.objects.all()
    serializer_class = StrategicGoalSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AgreementView(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


class IncidentView(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class ContractView(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ProviderView(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

            
class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

