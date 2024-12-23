from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.conf import settings


class LoginUseCase:
    USERNAME = settings.AUTH_USERNAME

    def __init__(self, request):
        self.request = request

    def execute(self):
        if self.request.user.is_authenticated:
            return redirect("reports:pending-reports")

        if self.request.method == 'POST':
            password = self.request.POST.get('password')
            user = User.objects.get(username=self.USERNAME)
            if user.check_password(password):
                login(self.request, user)
                return redirect("reports:pending-reports")

        return render(self.request, 'authentication/login.html')
