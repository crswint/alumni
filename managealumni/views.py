from django.views import generic
from .models import Alumni

# Create your views here.


class WelcomeView(generic.TemplateView):
    """This view will display the welcome page"""
    template_name = 'managealumni/welcome.html'


class AlumniList(generic.ListView):
    """This view will display the generic database alumni list"""
    model = Alumni


class LookingForWorkView(generic.ListView):
    """This view will display the alumni who have the lfw field checked as true."""
    model = Alumni
    template_name = 'managealumni/lookingforwork.html'
    context_object_name = 'lfw_alumni'
    queryset = Alumni.objects.filter(lfw=True)