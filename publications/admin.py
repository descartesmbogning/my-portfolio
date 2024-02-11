from django.contrib import admin
from .models import Publication

# Define the admin class for Publication
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'publication_date', 'published_in')
    list_filter = ('publication_date', 'published_in')
    search_fields = ('title', 'authors', 'abstract')
    fieldsets = (
        ('Publication Information', {
            'fields': ('title', 'authors', 'published_in', 'publication_date')
        }),
        ('Content', {
            'fields': ('abstract', 'keywords', 'doi', 'publication_link', 'pdf_file'),
            'classes': ('collapse',)
        }),
    )

# Note: Remember to make the necessary imports at the top if you're using inlines or RichTextField.
