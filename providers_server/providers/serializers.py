from .models import *
from rest_framework import serializers


class StrategicGoalSerializer(serializers.ModelSerializer):    
    class Meta:
        model = StrategicGoal
        fields = ('id', 'name')


class ServiceSerializer(serializers.ModelSerializer):

    strategic_goals = StrategicGoalSerializer(many=True, read_only=True)

    strategic_goals_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=StrategicGoal.objects.all(),
        source='strategic_goals')

    contract_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Service
        fields = (
            'id',
            'name',
            'service_category',
            'strategic_goals',
            'strategic_goals_ids',
            'contract_set')


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
    agreement_set = AgreementSerializer(many=True)
    task_set = TaskSerializer(many=True)
    incident_set = IncidentSerializer(many=True)
    services = ServiceSerializer(many=True, read_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Service.objects.all(),
        source='services')

    class Meta:
        model = Contract
        fields = (
            'name',
            'description',
            'contract_file',
            'agreement_set',
            'task_set',
            'incident_set',
            'services',
            'service_ids')
    
    def create(self, validate_data):

        agreement_set = validate_data.pop('agreement_set')
        task_set = validate_data.pop('task_set')

        contract = Contract.objects.create(**validate_data)

        for agreement in agreement_set:
            Agreement.objects.create(**agreement, contract=contract)
        
        for task in task_set:
            Task.objects.create(**task, contract=contract)

        return contract


class ProviderSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(many=True, read_only=True)
    
    class Meta:
        model = Provider
        fields = '__all__'