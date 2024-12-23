from modules.authentication.use_cases import LoginUseCase


def login(request):
    return LoginUseCase(request).execute()
