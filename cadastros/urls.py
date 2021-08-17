from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CampoCreate, AtividadeCreate

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
]