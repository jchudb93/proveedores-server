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
router.register('user', views.UserView)


contract_router = routers.NestedSimpleRouter(
    router,
    r'provider',
    lookup='provider')
contract_router.register(r'contracts', views.ContractView)

urlpatterns = [ 
    path('', include(router.urls)),
    path('', include(contract_router.urls)),
    path('provider_points/<int:id>/', views.ProviderPointsView.as_view()),
    path('provider_avgs/<int:pk>/', views.ProviderAvgPointsView.as_view()),
    path('provider_avgs/', views.AllProviderAvgPointsView.as_view()),
    path(
        'provider_contracts/<int:pk>',
        views.ProviderContractViewSet.as_view()),
    path(
        'service_providers/<int:pk>/',
        views.ServiceProviderViewSet.as_view()),
    path('login/<str:username>/<str:password>', views.UserLoginView.as_view())
]
