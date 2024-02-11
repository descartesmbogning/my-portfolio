from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import HomePage
# Uncomment the following line if you're using django-ckeditor
from ckeditor.fields import RichTextField

# Define the admin class for HomePage
@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    # Customize the list display
    list_display = ('welcome_message',)

    # Customize the form layout
    fieldsets = (
        ('General Information', {
            'fields': ('welcome_message', 'background_image')
        }),
        ('Additional Content', {
            'fields': ('additional_content',),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )

    # Example of how to integrate a RichTextField (uncomment if using django-ckeditor)
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'welcome_message':
            kwargs['widget'] = CKEditorWidget()
        return super().formfield_for_dbfield(db_field, **kwargs)

# Uncomment and modify this section if you have related models (e.g., Testimonial)
# class TestimonialInline(admin.TabularInline):
#     model = Testimonial

#     # You can add more customization to the inline here

#     # Then add the inline to the HomePageAdmin
#     inlines = [TestimonialInline,]

# Note: Remember to make the necessary imports at the top if you're using inlines or RichTextField.
