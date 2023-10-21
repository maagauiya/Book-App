from django.shortcuts import render
from rest_framework import generics, status, exceptions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from django.db.transaction import atomic
from django.contrib.auth import authenticate
from django.conf import settings

from ..serializers import CreateUserEmailSerializer, UserSerializer, LoginSerializer
from .tasks import send_activation_mail
from ..models import User
from .utils import verify_token, generate_token


class RegisterByEmailView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CreateUserEmailSerializer

    def create(self, request, *args, **kwargs):
        """Registration by email"""
        with atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            created_user = serializer.save()
            send_activation_mail.apply_async(args=(created_user.email, created_user.activate_token))
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserActivateView(generics.RetrieveAPIView):
    """Activate user using hash"""

    def retrieve(self, request, *args, **kwargs):
        activate_token = kwargs.get('token')
        user = User.objects.filter(activate_token=activate_token).last()
        if not user:
            return Response({"msg": "Hash inactive or user not found"}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        data = UserSerializer(user).data

        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class LoginByEmailView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        """Get user by token"""
        with atomic():
            authorization_header = request.headers.get('Authorization', "")
            if authorization_header and authorization_header.startswith('Bearer '):
                access_token = authorization_header.split(' ')[1]
                if access_token:
                    try:
                        validated_token = verify_token(access_token)
                        user_id = validated_token["user_id"]
                    except Exception as e:
                        return Response({'error_code': 'TOKEN_INVALID',
                                         'detail': str(e)},
                                        status=401)
                    if user_id:
                        user = User.objects.filter(id=user_id).last()
                        access = generate_token(
                            user,
                            settings.JWT_ACCESS_TOKEN_LIFETIME,
                        )
                        refresh = generate_token(
                            user,
                            settings.JWT_REFRESH_TOKEN_LIFETIME,
                            'refresh'
                        )
                        user_data = UserSerializer(User.objects.get(pk=user_id).person.first()).data
                        user_data['access'] = access
                        user_data['refresh'] = refresh
                        return Response({'user_data': user_data})

            """Authorization by email - returns token"""
            serializer = self.get_serializer(data=request.data)

            if not serializer.is_valid():
                return Response({'error_code': 'VALIDATION_ERROR',
                                 'detail': serializer.errors},
                                status=400)

            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(request=request,
                                username=email,
                                password=password)
            if user:
                if user.is_active:
                    access = generate_token(
                        user,
                        settings.JWT_ACCESS_TOKEN_LIFETIME,
                    )
                    refresh = generate_token(
                        user,
                        settings.JWT_REFRESH_TOKEN_LIFETIME,
                        'refresh'
                    )
                    user_data = UserSerializer(user).data
                    user_data['access'] = access
                    user_data['refresh'] = refresh
                    return Response(
                        {
                            'user_data': user_data,
                        }
                    )

                raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
            raise exceptions.AuthenticationFailed(_('Invalid email/password.'))
