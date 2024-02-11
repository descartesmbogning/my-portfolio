from django.contrib import admin
from .models import BlogPost

# Define the admin class for BlogPost
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    list_filter = ('publish_date', 'author')
    search_fields = ('title', 'content')
    readonly_fields = ('publish_date',)  # Add this line
    fieldsets = (
        ('Blog Post Information', {
            'fields': ('title', 'author')  # Removed 'publish_date' from here
        }),
        ('Content', {
            'fields': ('featured_image', 'content', 'excerpt'),
            'classes': ('collapse',)
        }),
        ('Categorization', {
            'fields': ('categories', 'tags'),
            'classes': ('collapse',)
        }),
    )

# blog/admin.py

#admin.site.register(BlogPost)

