from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.utils import actions
from .models import Book, Bookmark
from .serializers import BookmarkSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class BookMarkActionHandler(actions.BaseActionHandler):
    model_class = Book
    action = 'add_to_bookmark'

    def action_save(self):
        existing_bookmark = Bookmark.objects.filter(
            user=self.request.user,
            book=self.object
        ).first()
        if existing_bookmark:
            return Response(
                {"msg": "Bookmark already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        bookmark_instance = Bookmark.objects.create(
            user=self.request.user,
            book=self.object
        )
        serializer = BookmarkSerializer(bookmark_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def action_remove(self):
        bookmark_instance = Bookmark.objects.filter(
            user=self.request.user,
            book=self.object
        ).first()
        if not bookmark_instance:
            return Response(
                {"msg": "Bookmark not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        bookmark_instance.delete()
        return Response(status=status.HTTP_200_OK)

