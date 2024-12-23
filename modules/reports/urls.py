from django.urls import path

from modules.reports.views import (
  index,
  post_report,
  pending_reports,
  reports,
  report,
  approve_report,
  reject_report
)

app_name = 'reports'

urlpatterns = [
    path('', index, name='index'),
    path('pos-denuncia/', post_report, name='post-report'),
    path('denuncias/pendentes/', pending_reports, name='pending-reports'),
    path('denuncias/', reports, name='reports'),
    path('denuncia/<int:report_id>/', report, name='report'),
    path('denuncia/aprovar/<int:report_id>/', approve_report, name='approve-report'),
    path('denuncia/rejeitar/<int:report_id>/', reject_report, name='reject-report'),
]
