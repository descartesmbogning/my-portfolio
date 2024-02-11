
from django.views.generic import ListView
from .models import PortfolioItem

class PortfolioListView(ListView):
    model = PortfolioItem
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'portfolio_items'
    paginate_by = 10  # Optional: if you want to paginate the portfolio items
    # Add any additional filtering or search logic here



# publications/views.py
from django.shortcuts import render

def publications_list(request):
    # Your view logic here for the publications list
    return render(request, 'publications/portfolio_list.html')