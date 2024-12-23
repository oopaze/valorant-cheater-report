from django.urls import path

from modules.authentication.views import login

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
]
