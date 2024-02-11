from django.contrib import admin
from .models import ContactMessage

# Define the admin class for ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_date')
    list_filter = ('sent_date',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'sent_date')
    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email', 'sent_date')
        }),
        ('Message', {
            'fields': ('subject', 'message'),
            'classes': ('collapse',)
        }),
    )
    def has_add_permission(self, request):
        # Disable the ability to add new messages from the admin
        return False
