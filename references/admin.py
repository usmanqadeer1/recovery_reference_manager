from django.contrib import admin
from .models import Category, Reference, MediaFile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['reference_number', 'title', 'tariff', 'age', 'amount', 'created_at', 'updated_at']
    search_fields = ['reference_number', 'title', 'description', 'tariff']
    list_filter = ['created_at', 'updated_at', 'tariff']
    readonly_fields = ['created_at', 'updated_at']
    fields = ['reference_number', 'title', 'tariff', 'age', 'amount', 'description', 'remarks', 'created_at', 'updated_at']

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ['reference', 'get_filename', 'media_type', 'uploaded_at']
    list_filter = ['media_type', 'categories', 'uploaded_at']
    search_fields = ['reference__reference_number', 'reference__title']
    filter_horizontal = ['categories']
    readonly_fields = ['uploaded_at']
    
    def get_filename(self, obj):
        return obj.get_filename()
    get_filename.short_description = 'Filename'
