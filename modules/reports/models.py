from django.db import models
from datetime import timedelta


class Report(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        OUTDATED = 'outdated', 'Outdated'

    nickname = models.CharField(max_length=255)
    evidence_video = models.FileField(
        upload_to='evidence_videos/'
    )
    description = models.TextField(blank=True, null=True, default='')
    streamer_handle = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=''
    )
    platform = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=''
    )
    discord = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=''
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING.value,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    approved_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)

    approved_by = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='approved_reports'
    )
    rejected_by = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='rejected_reports'
    )

    @property
    def report_retention_policy(self):
        return self.approved_at + timedelta(7)
