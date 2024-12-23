from django.shortcuts import render

from modules.reports.models import Report
from common.use_cases import AuthenticatedUseCase


class ListPendingReportsUseCase(AuthenticatedUseCase):
    def __init__(self, request):
        self.request = request

    def _get_queryset(self, approved=False):
        if approved:
            return Report.objects.filter(status=Report.Status.APPROVED.value)
        return Report.objects.filter(status=Report.Status.PENDING.value)

    def _get_message(self):
        if self.request.GET.get('type') == 'approved':
            return {
                "message": "Denúncia aprovada com sucesso!",
                "tags": "success",
            }

        if self.request.GET.get('type') == 'rejected':
            return {
                "message": "Denúncia rejeitada com sucesso!",
                "tags": "success",
            }

    def execute(self, approved=False):
        if (response := self.validate_user()) and not approved:
            return response

        message = self._get_message()
        return render(
            self.request,
            f"reports/{'reports.html' if approved else 'pending-reports.html'}",
            {
                "reports": self._get_queryset(approved),
                "messages": [message] if message else [],
            }
        )
