from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'rating', 'display_book_name', 'display_user_full_name']
    search_fields = ['book__name']
    autocomplete_fields = ['book', 'user']

    def display_book_name(self, obj):
        return obj.book.name
    display_book_name.short_description = 'Book Name'

    def display_user_full_name(self, obj):
        return obj.user.full_name
    display_user_full_name.short_description = 'User Full Name'
