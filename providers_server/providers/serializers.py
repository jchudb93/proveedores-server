from .models import *
from rest_framework import serializers


class StrategicGoalSerializer(serializers.ModelSerializer):    
    class Meta:
        model = StrategicGoal
        fields = ('id', 'name')


class ServiceSerializer(serializers.ModelSerializer):

    strategic_goals = StrategicGoalSerializer(read_only=True, many=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'service_category', 'strategic_goals')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    agreement = AgreementSerializer(many=True, read_only=True)
    task = TaskSerializer(many=True, read_only=True)
    incident = IncidentSerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Contract
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(many=True, read_only=True)
    
    class Meta:
        model = Provider
        fields = '__all__'