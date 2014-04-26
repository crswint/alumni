from django.conf.urls import patterns, include, url
from .views import WelcomeView, AlumniList, LookingForWorkView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc.views.home', name='home'),
    # url(r'^gisc/', include('gisc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^welcome$', WelcomeView.as_view(), name='welcome'),
    url(r'^alumni$', AlumniList.as_view(), name='alumnilist'),
    url(r'^lfw$', LookingForWorkView.as_view(), name='lfw'),
)
