from django.db import models

class Publication(models.Model):
    # Title of the publication
    title = models.CharField(max_length=400)

    # List of authors
    authors = models.TextField()

    # Publication date
    publication_date = models.DateField()

    # Name of the journal or conference
    published_in = models.CharField(max_length=200)

    # Abstract of the publication
    abstract = models.TextField()

    # Keywords for the publication
    keywords = models.CharField(max_length=200, blank=True)

    # Link to the publication (if available online)
    publication_link = models.URLField(blank=True)

    # Digital Object Identifier (DOI)
    doi = models.CharField(max_length=100, blank=True)

    # PDF file of the publication (optional)
    pdf_file = models.FileField(upload_to='publications/media/publication_pdfs/', blank=True, null=True)

    # def __str__(self):
    #     # This will help identify each instance of Publication in the Django admin
    #     return self.title


    def get_absolute_url(self):
        return reverse('publication_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.title} by {self.authors}"


# Note: Remember to run 'python manage.py makemigrations' and 'python manage.py migrate'
# after creating or modifying your models.
