from rest_framework.serializers import Serializer, ModelSerializer, CharField, ValidationError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserRegistrSerializer(ModelSerializer):

    password2 = CharField()
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
 
    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:

            raise ValidationError({password: "Пароль не совпадает"})

        user.set_password(password)

        user.save()

        return user



class IssueTokenRequestSerializer(Serializer):
    model = User

    username = CharField(required=True)
    password = CharField(required=True)


class TokenSeriazliser(ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']
