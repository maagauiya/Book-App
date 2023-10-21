from django.contrib import admin

from .models import Book, Bookmark


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'display_genres', 'display_authors','published_date']
    search_fields = ['title']
    autocomplete_fields = ['genres', 'authors']

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all() if genre.name])

    display_genres.short_description = 'Genres'

    def display_authors(self, obj):
        return ", ".join([author.full_name for author in obj.authors.all() if author.full_name])

    display_authors.short_description = 'Authors'


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'display_book_title','display_user_username']
    search_fields = ['user__username', 'book__title']
    autocomplete_fields = ['user', 'book']

    def display_book_title(self, obj):
        return obj.book.title

    display_book_title.short_description = 'Book Title'

    def display_user_username(self, obj):
        return obj.user.username

    display_user_username.short_description = 'Username'

