from django.contrib import admin
from .models import ProfessionalBio, Skill, Education

# Define the admin class for ProfessionalBio
@admin.register(ProfessionalBio)
class ProfessionalBioAdmin(admin.ModelAdmin):
    list_display = ('introduction',)
    fieldsets = (
        ('Introduction', {
            'fields': ('introduction', 'biography')
        }),
        ('Image', {
            'fields': ('headshot_image',),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )

# Define the admin class for Skill
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency_level')
    list_filter = ('proficiency_level',)
    search_fields = ('name',)

# Define the admin class for Education
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year_completed')
    list_filter = ('year_completed', 'institution')
    search_fields = ('degree', 'institution')

# Note: Remember to make the necessary imports at the top if you're using inlines or RichTextField.
