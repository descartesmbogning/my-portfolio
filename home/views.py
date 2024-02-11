
from django.views.generic import TemplateView
from publications.models import Publication
from projects.models import Project
from blog.models import BlogPost
from .models import HomePage  # If you have a model for dynamic home page content
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_page_content'] = HomePage.objects.latest('updated')  # If you have a model storing home page content
        context['latest_publications'] = Publication.objects.all().order_by('-publication_date')[:1]  # Latest 3 publications
        context['current_project'] = Project.objects.all().order_by('-date_or_duration').first()  # Most recent project
        context['latest_blog_posts'] = BlogPost.objects.all().order_by('-publish_date')[:1]  # Latest 3 blog posts
        return context




def privacy_policy(request):
    # Add your logic here if any
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    # Add your logic here if any
    return render(request, 'terms_of_service.html')


def home_page(request):
    # Your view logic here
    
    return render(request, 'home/home_page.html')
