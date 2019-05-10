from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('strategic_goal', views.StrategicGoalView)
router.register('service', views.ServiceView)
router.register('task', views.TaskView)
router.register('incident', views.IncidentView)
router.register('agreement', views.AgreementView)
router.register('contract', views.ContractView)
router.register('provider', views.ProviderView)
router.register('supplier', views.SupplierView)

urlpatterns = [ 
    path('', include(router.urls))
]
