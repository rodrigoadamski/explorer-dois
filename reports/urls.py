from django.urls import path, include
from rest_framework import routers
from .views import ReportViewSet, DadosAmbientaisView, DadosAmbientaisTemplateView

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dados-ambientais/', DadosAmbientaisView.as_view(), name='dados-ambientais-api'),
]