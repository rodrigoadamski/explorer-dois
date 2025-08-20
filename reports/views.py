from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
import json
import requests
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by("-criado_em")
    serializer_class = ReportSerializer


@method_decorator(csrf_exempt, name='dispatch')
class DadosAmbientaisView(View):
    """View para buscar dados ambientais do INPE"""
    
    def get_dados_ambientais_completos(self, lat: float, lon: float, cidade: str):
        """Busca dados ambientais simulados (mockados)"""
        return {
            'queimadas': [],  # Lista vazia por enquanto
            'meteorologia': {
                'cidade': cidade,
                'temperatura': 25.5,
                'umidade': 65,
                'pressao': 1013.25,
                'vento_velocidade': 12.5,
                'vento_direcao': 'SE',
                'descricao': 'Parcialmente nublado',
                'atualizado_em': datetime.now().isoformat()
            },
            'qualidade_ar': {
                'cidade': cidade,
                'indice_qualidade': 45,  # Bom
                'categoria': 'Boa',
                'pm25': 12.5,  # µg/m³
                'pm10': 25.0,  # µg/m³
                'o3': 45.0,    # ppb
                'no2': 15.0,   # ppb
                'atualizado_em': datetime.now().isoformat()
            },
            'coordenadas': {
                'lat': lat,
                'lon': lon
            },
            'atualizado_em': datetime.now().isoformat()
        }
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            lat = float(data.get('lat'))
            lon = float(data.get('lon'))
            cidade = data.get('cidade', 'São Paulo')
            
            # Buscar dados ambientais
            dados = self.get_dados_ambientais_completos(lat, lon, cidade)
            
            return JsonResponse({
                'success': True,
                'dados': dados
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    
    def get(self, request):
        """Endpoint para testar a API"""
        return JsonResponse({
            'message': 'API de dados ambientais do INPE',
            'endpoints': {
                'POST /api/dados-ambientais/': 'Buscar dados por coordenadas',
                'GET /api/dados-ambientais/': 'Informações da API'
            }
        })


class DadosAmbientaisTemplateView(TemplateView):
    """View para renderizar o template de dados ambientais"""
    template_name = 'reports/dados_ambientais.html'