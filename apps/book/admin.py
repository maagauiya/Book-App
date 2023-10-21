from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'display_genres', 'display_authors']
    search_fields = ['title']
    autocomplete_fields = ['genres', 'authors']

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all() if genre.name])

    display_genres.short_description = 'Genres'

    def display_authors(self, obj):
        return ", ".join([author.full_name for author in obj.authors.all() if author.full_name])

    display_authors.short_description = 'Authors'


