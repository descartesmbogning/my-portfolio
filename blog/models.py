from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)

    # Author of the blog post (linked to the User model)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Date the blog post was published
    publish_date = models.DateField(auto_now_add=True)

    # Featured image for the blog post (optional)
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    # Content of the blog post
    content = models.TextField()

    # Excerpt or summary of the blog post
    excerpt = models.TextField()

    # Categories or tags for the blog post (optional)
    categories = models.CharField(max_length=200, blank=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        # This will help identify each instance of BlogPost in the Django admin
        return self.title

# Note: Remember to run 'python manage.py makemigrations' and 'python manage.py migrate'
# after creating or modifying your models.




