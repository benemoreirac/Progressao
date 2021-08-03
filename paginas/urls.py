from django.urls import path
from django.urls.resolvers import URLPattern

from .views import IndexView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]