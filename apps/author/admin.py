from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'first_name', 'last_name', 'patronymic']
    search_fields = ['first_name']

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name} {obj.patronymic}".strip()

    full_name.short_description = 'Full name'
