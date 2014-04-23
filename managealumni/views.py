from django.views import generic
from .models import Alumni

# Create your views here.


class WelcomeView(generic.TemplateView):
    template_name = 'managealumni/welcome.html'


class AlumniList(generic.ListView):
    model = Alumni