from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):  # JUST FOR ADMIN USERS
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

