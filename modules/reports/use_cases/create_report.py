from django.shortcuts import render, redirect

from modules.reports.forms import ReportForm


class CreateReportUseCase:
    def __init__(self, request):
        self.request = request
        self.form = ReportForm(request.POST, request.FILES)

    def execute(self):
        is_valid = self.form.is_valid()

        if self.form.is_valid():
            self.form.save()
            return redirect('reports:post-report')

        return render(self.request, 'index.html', {
            "errors": self.form.errors,
            "values": {} if is_valid else self.form.data,
            "files": self.form.files,
        })
