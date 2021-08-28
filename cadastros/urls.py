from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CampoCreate, AtividadeCreate, StatusCreate, ClasseCreate, CampusCreate, ProgressaoCreate, SituacaoCreate, ComprovanteCreate, ValidacaoCreate
from .views import CampoUpdate, AtividadeUpdate, StatusUpdate, ClasseUpdate, CampusUpdate, ProgressaoUpdate, SituacaoUpdate, ComprovanteUpdate, ValidacaoUpdate, ServidorUpdate
from .views import CampoDelete, AtividadeDelete, StatusDelete, ClasseDelete, CampusDelete, ProgressaoDelete, SituacaoDelete, ComprovanteDelete, ValidacaoDelete
from .views import CampoList, AtividadeList, StatusList, ClasseList, CampusList, ProgressaoList, SituacaoList, ComprovanteList, ValidacaoList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/status/', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastrar/classe/', ClasseCreate.as_view(), name='cadastrar-classe'),
    path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),
    path('cadastrar/progressao/', ProgressaoCreate.as_view(), name="cadastrar-progressao"),
    path('cadastrar/situacao/', SituacaoCreate.as_view(), name="cadastrar-situacao"),
    path('cadastrar/comprovante/', ComprovanteCreate.as_view(), name="cadastrar-comprovante"),
    path('validar/comprovante/<int:id_comprovante>', ValidacaoCreate.as_view(), name="validar-comprovante"),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name='editar-status'),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name='editar-classe'),
    path('editar/campus/<int:pk>/', CampusUpdate.as_view(), name='editar-campus'),
    path('editar/progressao/<int:pk>/', ProgressaoUpdate.as_view(), name="editar-progressao"),
    path('editar/situacao/<int:pk>/', SituacaoUpdate.as_view(), name="editar-situacao"),
    path('editar/comprovante/<int:pk>/', ComprovanteUpdate.as_view(), name="editar-comprovante"),
    path('alterar/validacao/comprovante/<int:id_comprovante>', ValidacaoUpdate.as_view(), name="atualizar-validacao-comprovante"),
    
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('excluir/status/<int:pk>/', StatusDelete.as_view(), name='excluir-status'),
    path('excluir/classe/<int:pk>/', ClasseDelete.as_view(), name='excluir-classe'),
    path('excluir/campus/<int:pk>/', CampusDelete.as_view(), name='excluir-campus'),
    path('excluir/progressao/<int:pk>/', ProgressaoDelete.as_view(), name="excluir-progressao"),
    path('excluir/situacao/<int:pk>/', SituacaoDelete.as_view(), name="excluir-situacao"),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name="excluir-atividade"),
    path('excluir/comprovante/<int:pk>/', ComprovanteDelete.as_view(), name="excluir-comprovante"),

    path('listar/campos/', CampoList.as_view(), name='listar-campo'),
    path('listar/atividade/', AtividadeList.as_view(), name='listar-atividade'),
    path('listar/status/', StatusList.as_view(), name='listar-status'),
    path('listar/classe/', ClasseList.as_view(), name='listar-classe'),
    path('listar/campus/', CampusList.as_view(), name='listar-campus'),
    path('listar/situacoes/', SituacaoList.as_view(), name="listar-situacao"),
    path('listar/progressoes/', ProgressaoList.as_view(), name="listar-progressao"),
    path('listar/comprovantes/', ComprovanteList.as_view(), name="listar-comprovante"),    
]