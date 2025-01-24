from django.contrib import admin
from myapp.models import MarkdownFile

@admin.register(MarkdownFile)

class MarkdownFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'createdAt', 'updatedAt')
    search_fields = ('name',)
