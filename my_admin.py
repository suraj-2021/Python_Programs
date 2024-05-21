from django.contrib import admin
from .models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')  # Update the field names
    search_fields = ['field1', 'field2']  # Update the field names for search
    list_filter = ('field1', 'field2')  # Update the field names for filters
