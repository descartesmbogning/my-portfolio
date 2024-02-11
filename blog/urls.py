from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),  # List view for all blog posts
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  # Detail view for a single post
]
