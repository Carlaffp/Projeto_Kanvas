from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email', 'username', 'password', 'is_superuser']
        extra_kwargs = {'password':{'write_only':True}}
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="user with this email already exists."
            )
        ],
    ) 

    def create(self, validated_data):
        if validated_data.get("is_superuser"):
            user = Account.objects.create_superuser(**validated_data)
        else:
            user = Account.objects.create_user(**validated_data)
        return user
