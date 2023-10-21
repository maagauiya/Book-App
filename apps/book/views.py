from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Bookmark
from .serializers import BookSerializer, BookRetrieveSerializer, BookListSerializer, BookmarkSerializer
from .filters import BookFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookRetrieveSerializer
        elif self.action == 'list':
            return BookListSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_bookmark(request):
    bookmarks = request.user.user_bookmarks.all()
    serializer = BookmarkSerializer(bookmarks, many=True)
    return Response(serializer.data)


