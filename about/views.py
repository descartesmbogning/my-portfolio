
from django.views.generic import TemplateView
from .models import ProfessionalBio, Skill, Education

class AboutView(TemplateView):
    template_name = 'about/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['professional_bio'] = ProfessionalBio.objects.first()  # Assuming only one bio
        context['skills'] = Skill.objects.all()  # Get all skills
        context['educations'] = Education.objects.all()  # Get all education records
        return context


# publications/views.py
from django.shortcuts import render

def publications_list(request):
    # Your view logic here for the publications list
    return render(request, 'publications/about_page.html')