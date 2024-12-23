from django.core.management.base import BaseCommand
from django.utils.timezone import now

from modules.reports.models import Report


class Command(BaseCommand):
    help = 'Starts a routine to clean reports'

    def handle(self, *args, **options):
        reports = Report.objects.filter(status=Report.Status.APPROVED.value)
        to_update_reports = []

        for report in reports:
            if report.report_retention_policy < now():
                report.status = Report.Status.OUTDATED.value
                to_update_reports.append(report)

        number_of_reports = Report.objects.bulk_update(to_update_reports, ['status'])
        self.stdout.write(self.style.SUCCESS(f'{number_of_reports} reports updated'))
