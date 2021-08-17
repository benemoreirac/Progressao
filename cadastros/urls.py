from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CampoCreate, AtividadeCreate, CampusCreate, ClassesCreate, StatusCreate
from .views import CampoUpdate, AtividadeUpdate, StatusUpdate, ClassesUpdate, CampusUpdate
from .views import CampoDelete, AtividadeDelete, StatusDelete, ClassesDelete, CampusDelete

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/status/', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastrar/classe/', ClassesCreate.as_view(), name='cadastrar-classe'),
    path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name='editar-status'),
    path('editar/classe/<int:pk>/', ClassesUpdate.as_view(), name='editar-classe'),
    path('editar/campus/<int:pk>/', CampusUpdate.as_view(), name='editar-campus'),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('excluir/status/<int:pk>/', StatusDelete.as_view(), name='excluir-status'),
    path('excluir/classe/<int:pk>/', ClassesDelete.as_view(), name='excluir-classe'),
    path('excluir/campus/<int:pk>/', CampusDelete.as_view(), name='excluir-campus'),
]