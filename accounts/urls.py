from django.urls import path
from accounts.views import AccontView, LoginView


urlpatterns = [
    path("accounts/", AccontView.as_view()),
    path("login/", LoginView.as_view())
]
