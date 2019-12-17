from django.contrib import admin
from .models import LicenseBrickDesign


@admin.register(LicenseBrickDesign)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'key', 'computer_name', )
    list_display_links = ('email',)
    search_fields = ('email', 'computer_name',)
