from django.urls import path
from django.urls.resolvers import URLPattern
from .views import AtividadeList, CampoCreate, AtividadeCreate, CampoList, CampusCreate, ClassesCreate, StatusCreate, ProgressaoCreate
from .views import CampoUpdate, AtividadeUpdate, StatusUpdate, ClassesUpdate, CampusUpdate, ProgressaoUpdate
from .views import CampoDelete, AtividadeDelete, StatusDelete, ClassesDelete, CampusDelete, ProgressaoDelete
from .views import CampoList, AtividadeList, ProgressaoList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/progressao/', ProgressaoCreate.as_view(), name="cadastrar-progressao"),
    path('cadastrar/status/', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastrar/classe/', ClassesCreate.as_view(), name='cadastrar-classe'),
    path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/progressao/<int:pk>/', ProgressaoUpdate.as_view(), name="editar-progressao"),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name='editar-status'),
    path('editar/classe/<int:pk>/', ClassesUpdate.as_view(), name='editar-classe'),
    path('editar/campus/<int:pk>/', CampusUpdate.as_view(), name='editar-campus'),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('excluir/status/<int:pk>/', StatusDelete.as_view(), name='excluir-status'),
    path('excluir/classe/<int:pk>/', ClassesDelete.as_view(), name='excluir-classe'),
    path('excluir/campus/<int:pk>/', CampusDelete.as_view(), name='excluir-campus'),
    path('excluir/progressao/<int:pk>/', ProgressaoDelete.as_view(), name="excluir-progressao"),

    path('listar/campos/', CampoList.as_view(), name='listar-campo'),
    path('listar/atividade/', AtividadeList.as_view(), name='listar-atividade'),
    path('listar/status/', AtividadeList.as_view(), name='listar-status'),
    path('listar/classe/', AtividadeList.as_view(), name='listar-classe'),
    path('listar/campus/', AtividadeList.as_view(), name='listar-campus'),
    path('listar/progressoes/', ProgressaoList.as_view(), name="listar-progressao"),

]