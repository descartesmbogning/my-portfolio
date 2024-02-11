from django.urls import path
from .views import PublicationsListView  # Import your view

urlpatterns = [
    path('', PublicationsListView.as_view(), name='publications_list'),  # The 'name' parameter should match the name used in your template
]
