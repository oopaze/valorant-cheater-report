from django.shortcuts import render
from modules.reports.use_cases import (
  CreateReportUseCase,
  ListPendingReportsUseCase,
  ApproveRejectReportUseCase,
  GetReportUseCase,
)


def index(request):
    if request.method == 'POST':
        return CreateReportUseCase(request).execute()
    return render(request, 'index.html')


def post_report(request):
    return render(request, 'reports/post-report.html')


def pending_reports(request):
    return ListPendingReportsUseCase(request).execute()


def reports(request):
    return ListPendingReportsUseCase(request).execute(approved=True)


def report(request, report_id):
    return GetReportUseCase(request).execute(report_id)


def approve_report(request, report_id):
    return ApproveRejectReportUseCase(request).execute(report_id)


def reject_report(request, report_id):
    return ApproveRejectReportUseCase(request).execute(
        report_id,
        approve=False
    )
