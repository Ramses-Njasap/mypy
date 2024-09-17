from django.contrib import admin
from .models import TestModel

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'owner')  # Adjust fields as needed
    search_fields = ('name',)  # Add fields to be searchable
    list_filter = ('is_published', 'owner')  # Add filters for the list view

# Alternatively, you can register the model using:
# admin.site.register(TestModel, TestModelAdmin)
