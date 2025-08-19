from django.urls import path, include
from rest_framework import routers
from .views import ReportViewSet, ReportsMapView

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('map/', ReportsMapView.as_view(), name='reports-map'),
]