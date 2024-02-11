from django.db import models

class ContactMessage(models.Model):
    # Name of the person sending the message
    name = models.CharField(max_length=100)

    # Email of the person sending the message
    email = models.EmailField()

    # Subject of the message
    subject = models.CharField(max_length=200)

    # Content of the message
    message = models.TextField()

    # Date the message was sent
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This will help identify each instance of ContactMessage in the Django admin
        return f"Message from {self.name} - {self.subject}"

# Note: Remember to run 'python manage.py makemigrations' and 'python manage.py migrate'
# after creating or modifying your models.
