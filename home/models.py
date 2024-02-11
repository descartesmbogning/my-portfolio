from django.db import models

class HomePage(models.Model):
    #name = models.CharField(max_length=100)
    
    # A welcome message on the home page
    welcome_message = models.TextField()
    #welcome_message2 = models.TextField()
    # Background image for the home page (optional)
    background_image = models.ImageField(upload_to='home/media/', blank=True, null=True)

    # Any additional content you want to be able to update from the admin
    additional_content = models.TextField(blank=True, null=True)
    
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # This will help identify each instance of HomePage in the Django admin
        return "Home Page Content"

# Note: Remember to run 'python manage.py makemigrations' and 'python manage.py migrate'
# after creating or modifying your models.
