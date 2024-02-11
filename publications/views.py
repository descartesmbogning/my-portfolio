
from django.views.generic import ListView
from .models import Publication

class PublicationsListView(ListView):
    model = Publication
    template_name = 'publications/publications_list.html'
    context_object_name = 'publications'
    paginate_by = 200  # Optional: if you want to paginate the publications
    # Add any additional filtering or search logic here
    ordering = ['-publication_date']  # Adjust the field name as per your model (e.g., '-publication_date' for most recent)

# publications/views.py
from django.shortcuts import render

def publications_list(request):
    # Your view logic here for the publications list
    return render(request, 'publications/publications_list.html')
