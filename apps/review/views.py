from rest_framework import viewsets

from .models import Review
from .serializers import ReviewSerializer


from rest_framework import status
from rest_framework.response import Response


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def check_user_permission(self, review):
        if review.user != self.request.user:
            return Response(
                {"msg": "You do not have permission to update"},
                status=status.HTTP_403_FORBIDDEN
            )
        return True

    def perform_create(self, serializer):
        super(ReviewViewSet, self).perform_create(serializer)
        book = serializer.instance.book
        book.recalculate_average_rating()

    def perform_update(self, serializer):
        super(ReviewViewSet, self).perform_update(serializer)
        book = serializer.instance.book
        book.recalculate_average_rating()

    def perform_destroy(self, instance):
        book = instance.book
        super(ReviewViewSet, self).perform_destroy(instance)
        book.recalculate_average_rating()
