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
    
    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.dateLimit = validated_data.get(
            'dateLimit',
            instance.dateLimit)
        instance.dateEnd = validated_data.get('dateEnd', instance.dateEnd)
        instance.notification = validated_data.get(
            'notification',
            instance.notification)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance


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


class ProviderSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Provider
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    agreement_contracts = AgreementSerializer(many=True)
    task_contracts = TaskSerializer(many=True)
    incident_contracts = IncidentSerializer(many=True, read_only=True)

    services = ServiceSerializer(many=True, read_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Service.objects.all())

    provider = ProviderSerializer(read_only=True)
    provider_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Provider.objects.filter(state__exact='Activo'))

    class Meta:
        model = Contract
        fields = (
            'id',
            'name',
            'description',
            'contract_file',
            'agreement_contracts',
            'state',
            'dateStart',
            'dateEnd',
            'task_contracts',
            'incident_contracts',
            'services',
            'service_ids',
            'percentage',
            'in_charge_points',
            'quality_points',
            'contract_points',
            'provider',
            'provider_id')
    
    def create(self, validate_data):

        agreement_contracts = validate_data.pop('agreement_contracts')
        task_contracts = validate_data.pop('task_contracts')
        service_ids = validate_data.pop('service_ids')
        provider_id = validate_data.pop('provider_id')
        contract = Contract.objects.create(
            **validate_data,
            provider=provider_id)

        for agreement in agreement_contracts:
            Agreement.objects.create(contract=contract, **agreement)
        
        for task in task_contracts:
            Task.objects.create(contract=contract, **task)
        
        for service_id in service_ids:
            
            contract.services.add(service_id)
        
        return contract


class ContractStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract


class ProviderStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
