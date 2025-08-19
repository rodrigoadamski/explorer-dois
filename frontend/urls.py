from django.urls import path
from .views import HomeView, ReportCreateView, ReportListView, ReportsMapView
from .views_auth import SignUpView


urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("reports/new/", ReportCreateView.as_view(), name="report-create"),
	path("reports/list/", ReportListView.as_view(), name="reports-list"),
	path("map/", ReportsMapView.as_view(), name="reports-map"),
	path("accounts/signup/", SignUpView.as_view(), name="signup"),
]

