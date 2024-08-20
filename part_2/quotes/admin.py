from django.contrib import admin
from .models import Author, Quote

# Регистрация моделей в админке
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'user')
    search_fields = ('text', 'author__name')
    list_filter = ('author', 'user')