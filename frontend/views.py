from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from reports.models import Report
from reports.forms import ReportForm


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


class ReportsMapView(TemplateView):
	template_name = "reports/map.html"

from django.shortcuts import render

# Create your views here.
