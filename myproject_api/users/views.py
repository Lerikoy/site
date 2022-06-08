from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserRegistrSerializer, IssueTokenRequestSerializer, TokenSeriazliser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


# @api_view()
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# def user(request: Request):
#     return Response({
#         'data': UserSerializer(request.user).data
#     })


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def Register_Users(request: Request):
#     data = []
#     serializer = RegistrationSerializer(data=request.data)
#     if serializer.is_valid():
#         account = serializer.save()
#         account.save()
#         token = Token.objects.create(user=account)
#         return Response(TokenSeriazliser(token).data)
#     else:
#         return Response(serializer.errors, status=400)

# Создаём класс RegistrUserView
@api_view(["POST"])
@permission_classes([AllowAny])
def Register_Users(request: Request):
    # Добавляем UserRegistrSerializer
    serializer = UserRegistrSerializer(data=request.data)
    # Создаём список data
    data = {}
    # Проверка данных на валидность
    if serializer.is_valid():
        # Сохраняем нового пользователя
        account = serializer.save()
        account.save()
        token = Token.objects.create(user=account)
        # Возвращаем что всё в порядке
        return Response(TokenSeriazliser(token).data, status=status.HTTP_200_OK)
    else: # Иначе
        # Присваиваем data ошибку
        data = serializer.errors
        # Возвращаем ошибку
        return Response(data)



@api_view(['POST'])
@permission_classes([AllowAny])
def Login_Users(request: Request):
    serializer = IssueTokenRequestSerializer(data=request.data)
    if serializer.is_valid():
        authenticated_user = authenticate(**serializer.validated_data)
        try:
            token = Token.objects.get(user=authenticated_user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=authenticated_user)
        return Response(TokenSeriazliser(token).data)
    else:
        return Response(serializer.errors, status=400)


# token d87dbae3d770fbebd407b2667809c4e8ddfbd1f6