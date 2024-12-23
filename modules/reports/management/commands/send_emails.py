from django.core.management.base import BaseCommand

from modules.reports.models import Report


class Command(BaseCommand):
    help = 'Send emails to Riot spamming the cheaters'

    def handle(self, *args, **options):
        reports = Report.objects.filter(status=Report.Status.APPROVED.value)

        for report in reports:
            self.stdout.write(self.style.SUCCESS(f'Sending email to {report.nickname}'))
