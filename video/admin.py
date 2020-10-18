from django.contrib import admin
from .models import File

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'filepath']

admin.site.register(File, FileAdmin)


