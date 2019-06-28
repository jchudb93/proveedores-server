from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import *
from .serializers import *

from django.db.models import Avg, Count


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
    

class UpdateContractState(generics.UpdateAPIView):
    
    queryset = Contract.objects.all()
    serializer_class = ContractStateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.state = request.data.get('state')
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class UpdateProviderState(generics.UpdateAPIView):

    queryset = Provider.objects.all()
    serializer_class = ProviderStateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.state = request.data.get('state')
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class UpdateContractQualification(generics.UpdateAPIView):

    queryset = Contract.objects.all()
    serializer_class = ContractQualificationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.in_charge_points = request.data.get('in_charge_points')
        instance.quality_points = request.data.get('quality_points')
        instance.contract_points = request.data.get('contract_points')
        instance.supplier_points = request.data.get('supplier_points')
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class ProviderPointsView(generics.ListAPIView):

    serializer_class = ContractPointsSerializer

    def get_queryset(self):

        provider = self.kwargs['id']
        queryset = Contract.objects.filter(
            provider_id=provider
            ).order_by(
                'dateStart'
                )
        return queryset


class ProviderAvgPointsView(generics.RetrieveAPIView):

    lookup_field = 'provider_avgs'
    serializer_class = ProviderAvgSerializer

    def get_object(self):

        provider = self.kwargs['pk']
        queryset = Contract.objects.filter(
            provider_id=provider
            ).aggregate(
                in_charge_points_avg=Avg('in_charge_points'),
                quality_points_avg=Avg('quality_points'),
                contract_points_avg=Avg('contract_points'),
                supplier_points_avg=Avg('supplier_points')
            )
        return queryset


class AllProviderAvgPointsView(generics.ListAPIView):

    serializer_class = ProviderAvgSerializer

    def get_queryset(self):

        queryset = Contract.objects.values('provider_id').all().annotate(
                in_charge_points_avg=Avg('in_charge_points'),
                quality_points_avg=Avg('quality_points'),
                contract_points_avg=Avg('contract_points'),
                supplier_points_avg=Avg('supplier_points')
            )
        return queryset


class ProviderContractViewSet(generics.ListAPIView):

    serializer_class = ContractSerializer

    def get_queryset(self):

        provider = self.kwargs['pk']
        queryset = Contract.objects.filter(provider_id=provider)

        return queryset


class ServiceProviderViewSet(generics.ListAPIView):

    serializer_class = ServiceProviderSerialzier

    def get_queryset(self):

        service = self.kwargs['pk']
        queryset = Contract.objects.filter(
            services=service
            ).values(
                'provider_id'
                ).annotate(
                    contract_count=Count('provider_id'))
        
        return queryset