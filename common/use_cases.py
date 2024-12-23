from django.shortcuts import redirect


class AuthenticatedUseCase:
    def __init__(self, request):
        self.request = request

    def validate_user(self):
        if not self.request.user.is_authenticated:
            return redirect('authentication:login')
