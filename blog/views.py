
from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_posts'
    paginate_by = 10  # Optional: if you want to paginate the blog posts
    # Add any additional filtering or search logic here

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog_post'


# publications/views.py
from django.shortcuts import render

def publications_list(request):
    # Your view logic here for the publications list
    return render(request, 'publications/blog_list.html')