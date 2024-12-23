from django.shortcuts import get_object_or_404, render

from modules.reports.models import Report


class GetReportUseCase:
    def __init__(self, request):
        self.request = request

    def execute(self, report_id):
        report = get_object_or_404(Report, id=report_id)
        return render(self.request, 'reports/report.html', {
            "report": report
        })
