from django.views import generic
from .models import Alumni

# Create your views here.


class WelcomeView(generic.TemplateView):
    template_name = 'managealumni/welcome.html'


class AlumniList(generic.ListView):
    model = Alumni


class LookingForWorkView(generic.ListView):
    model = Alumni
    template_name = 'managealumni/lookingforwork.html'
    context_object_name = 'lfw_alumni'
    queryset = Alumni.objects.filter(lfw=True)