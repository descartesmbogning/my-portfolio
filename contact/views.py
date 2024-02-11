
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import ContactMessage

class ContactFormView(FormView):
    template_name = 'contact/contact_page.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')  # Redirect to the contact page after successful submission

    def form_valid(self, form):
        # Save the form data to the database
        ContactMessage.objects.create(**form.cleaned_data)
        # Optionally, send an email notification
        # ...
        return super().form_valid(form)
    

    # publications/views.py
from django.shortcuts import render

def publications_list(request):
    # Your view logic here for the publications list
    return render(request, 'publications/contact_page.html')