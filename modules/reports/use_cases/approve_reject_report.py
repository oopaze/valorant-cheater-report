from django.shortcuts import redirect

from modules.reports.models import Report
from common.use_cases import AuthenticatedUseCase


class ApproveRejectReportUseCase(AuthenticatedUseCase):
    def __init__(self, request):
        self.request = request

    def _update_report_status(self, report_id, status):
        report = Report.objects.get(id=report_id)
        report.status = status

        if status == Report.Status.APPROVED.value:
            report.approved_at = report.updated_at
            report.approved_by = self.request.user
        else:
            report.rejected_at = report.updated_at
            report.rejected_by = self.request.user

        report.save()

    def execute(self, report_id, approve=True):
        if response := self.validate_user():
            return response

        status = (
            Report.Status.APPROVED.value
            if approve else
            Report.Status.REJECTED.value
        )
        self._update_report_status(report_id, status)
        return redirect('reports:pending-reports')
