from django.db import models

class PortfolioItem(models.Model):
    # Title of the portfolio item
    title = models.CharField(max_length=200)

    # Brief overview or summary of the portfolio item
    summary = models.TextField()

    # Detailed description of the portfolio item
    description = models.TextField()

    # Technologies or tools used in the portfolio item
    technologies = models.CharField(max_length=200)

    # Date or duration of the portfolio item
    date_or_duration = models.CharField(max_length=100)

    # Thumbnail or preview image of the portfolio item (optional)
    thumbnail_image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)

    # Link to the detailed case study or project (if available)
    case_study_link = models.URLField(blank=True)

    def __str__(self):
        # This will help identify each instance of PortfolioItem in the Django admin
        return self.title

# Note: Remember to run 'python manage.py makemigrations' and 'python manage.py migrate'
# after creating or modifying your models.
