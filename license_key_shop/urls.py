from django.urls import include, path, re_path
from rest_framework import routers
from .views import SalesInfoDateViewSet, SalesInfoTypeViewSet, RegisterUserViewSet


router = routers.DefaultRouter()
router.register(r'register-user', RegisterUserViewSet, basename="register-user")
router.register(r'sales-info-date', SalesInfoDateViewSet, basename="sales-info-date")
router.register(r'sales-info-type', SalesInfoTypeViewSet, basename="sales-info-type")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^nested_admin/', include('nested_admin.urls')),
]

