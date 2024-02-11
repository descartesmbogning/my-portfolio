
from django.views.generic import ListView
from .models import Project

class ProjectsListView(ListView):
    model = Project
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects'
    paginate_by = 10  # Optional: if you want to paginate the projects
    # Add any additional filtering or search logic here


# publications/views.py
from django.shortcuts import render

def publications_list(request):
    # Your view logic here for the publications list
    return render(request, 'publications/projects_list.html')