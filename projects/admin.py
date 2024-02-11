from django.contrib import admin
from .models import Project

# Define the admin class for Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_or_duration', 'technologies')
    list_filter = ('date_or_duration', 'technologies')
    search_fields = ('title', 'description', 'technologies')
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'summary', 'description', 'date_or_duration')
        }),
        ('Technical Details', {
            'fields': ('technologies',),
            'classes': ('collapse',)
        }),
        ('Media', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
        ('External Links', {
            'fields': ('project_link', 'repository_link'),
            'classes': ('collapse',)
        }),
    )

# Note: Remember to make the necessary imports at the top if you're using inlines or RichTextField.
