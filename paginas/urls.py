from django.urls import path
from django.urls.resolvers import URLPattern

from .views import IndexView, SobreView

urlpatterns = [
    path('home', IndexView.as_view(), name='home'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]