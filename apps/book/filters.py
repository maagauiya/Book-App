from django_filters import rest_framework as django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    genres = django_filters.CharFilter(field_name="genres__name")
    author_first_name = django_filters.CharFilter(field_name="authors__first_name")
    author_last_name = django_filters.CharFilter(field_name="authors__last_name")
    published_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ['genres', 'author_first_name', 'author_last_name', "published_date"]
