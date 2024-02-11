from django.db import models

class Project(models.Model):
    # Title of the project
    title = models.CharField(max_length=200)

    # Brief overview or summary of the project
    summary = models.TextField()

    # Detailed description of the project
    description = models.TextField()

    # Your role in the project
    role = models.CharField(max_length=200)

    # Results or impact of the project
    results = models.TextField()

    # Date or duration of the project
    date_or_duration = models.CharField(max_length=100)

    # Technologies or tools used in the project
    technologies = models.CharField(max_length=200)

    # Team members or collaborators (optional)
    team_members = models.TextField(blank=True)

    # Link to the project (if available online)
    project_link = models.URLField(blank=True)

    # Link to the code repository (if applicable)
    repository_link = models.URLField(blank=True)

    # Images or other media related to the project (optional)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        # This will help identify each instance of Project in the Django admin
        return self.title

# Note: Remember to run 'python manage.py makemigrations' and 'python manage.py migrate'
# after creating or modifying your models.
