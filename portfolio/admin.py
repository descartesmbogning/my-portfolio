from django.contrib import admin
from .models import PortfolioItem

# Define the admin class for PortfolioItem
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_or_duration', 'technologies')
    list_filter = ('date_or_duration', 'technologies')
    search_fields = ('title', 'description', 'technologies')
    fieldsets = (
        ('Portfolio Item Information', {
            'fields': ('title', 'summary', 'description', 'date_or_duration')
        }),
        ('Technical Details', {
            'fields': ('technologies',),
            'classes': ('collapse',)
        }),
        ('Media', {
            'fields': ('thumbnail_image',),
            'classes': ('collapse',)
        }),
        ('External Links', {
            'fields': ('case_study_link',),
            'classes': ('collapse',)
        }),
    )

# Note: Remember to make the necessary imports at the top if you're using inlines or RichTextField.
