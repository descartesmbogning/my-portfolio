from django.db import models

class ProfessionalBio(models.Model):
    # A brief introduction about you
    introduction = models.TextField()

    # Detailed biography
    biography = models.TextField()

    # Your professional headshot (optional)
    headshot_image = models.ImageField(upload_to='about_headshots/', blank=True, null=True)

    def __str__(self):
        # This will help identify each instance of ProfessionalBio in the Django admin
        return "Professional Biography"

class Skill(models.Model):
    # Name of the skill
    name = models.CharField(max_length=100)

    # (Optional) A short description of the skill
    description = models.TextField(blank=True, null=True)

    # (Optional) Level of proficiency with the skill
    proficiency_level = models.IntegerField(blank=True, null=True)

    def __str__(self):
        # This will help identify each instance of Skill in the Django admin
        return self.name

class Education(models.Model):
    # Degree or certification obtained
    degree = models.CharField(max_length=150)

    # Institution name
    institution = models.CharField(max_length=150)

    # Year of completion or range of years attended
    year_completed = models.CharField(max_length=50)

    def __str__(self):
        # This will help identify each instance of Education in the Django admin
        return f"{self.degree} from {self.institution}"

# Note: Remember to run 'python manage.py makemigrations' and 'python manage.py migrate'
# after creating or modifying your models.
