from rest_framework import viewsets
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Report
from .serializers import ReportSerializer
from .forms import ReportForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by("-criado_em")
    serializer_class = ReportSerializer


class ReportsMapView(TemplateView):
    template_name = "reports/map.html"


class HomeView(TemplateView):
    template_name = "reports/home.html"


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = "reports/report_list.html"
    context_object_name = "reports"
    ordering = ["-criado_em"]


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = "reports/report_form.html"
    success_url = reverse_lazy("reports-list")