from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('strategic_goal', views.StrategicGoalView)
router.register('service', views.ServiceView)
router.register('task', views.TaskView)
router.register('incident', views.IncidentView)
router.register('agreement', views.AgreementView)
router.register('contract', views.ContractView)
router.register('provider', views.ProviderView)
router.register('supplier', views.SupplierView)

contract_router = routers.NestedSimpleRouter(
    router,
    r'provider',
    lookup='provider')
contract_router.register(r'contracts', views.ContractView)

urlpatterns = [ 
    path('', include(router.urls)),
    path('', include(contract_router.urls))
]
