from django import forms

from modules.reports.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'nickname',
            'evidence_video',
            'description',
            'streamer_handle',
            'platform',
            'discord',
        ]
