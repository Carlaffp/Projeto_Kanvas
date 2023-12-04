from accounts.models import Account
from accounts.serializer import AccountSerializer
from rest_framework.generics import CreateAPIView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView


@extend_schema(
        tags = ['Criação de Usuários']
    )

class AccontView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


@extend_schema(
        tags = ['Autenticação']
    )


class LoginView(TokenObtainPairView):
    ...
