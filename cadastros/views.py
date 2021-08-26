from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Campo, Atividade, Status, Classe, Campus, Progressao, Situacao, Comprovante, Validacao, Servidor
from django.urls import reverse_lazy
from django.views.generic.list import ListView 

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# Create your views here.

class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    fields = ['nome','descricao']
    template_name ='cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')

class StatusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class ClassesCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'nível', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class CampusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Campus
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class ProgressaoCreate(CreateView):
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

class SituacaoCreate(CreateView):
    model = Situacao
    fields = ['status', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacao')

class ComprovanteCreate(CreateView):
    model = Comprovante
    fields = ['progressao', 'atividade',
              'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comprovante')

class ValidacaoCreate(CreateView):
    model = Validacao
    fields = ['quantidade', 'justificativa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-validacoes')

###### UPDATE ######

class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')

class StatusUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class ClassesUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'nível', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class CampusUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Campus
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class ProgressaoUpdate(LoginRequiredMixin, UpdateView):
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

class SituacaoUpdate(UpdateView):
    model = Situacao
    fields = ['status', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacao')

class ComprovanteUpdate(UpdateView):
    model = Comprovante
    fields = ['progressao', 'atividade',
              'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comprovante')

class ValidacaoUpdate(UpdateView):
    model = Validacao
    fields = ['quantidade', 'justificativa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-validacoes')

class ServidorUpdate(UpdateView):
    model = Servidor
    fields = ['nome_completo', 'siape', 'cpf', 'campus']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

###### DELETE ######

class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campo')

class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividade')

class StatusDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')

class ClassesDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')

class CampusDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Campus    
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')

class ProgressaoDelete(LoginRequiredMixin, DeleteView):
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

class SituacaoDelete(DeleteView):
    model = Situacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-situacao')

class ComprovanteDelete(DeleteView):
    model = Comprovante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comprovante')

class ValidacaoDelete(DeleteView):
    model = Validacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-validacao')


###### LIST ######

class CampoList(LoginRequiredMixin, ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'
    login_url = reverse_lazy('login')

class AtividadeList(LoginRequiredMixin, ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'
    login_url = reverse_lazy('login')

class StatusList(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'cadastros/listas/status.html'
    login_url = reverse_lazy('login')

class ClasseList(LoginRequiredMixin, ListView):
    model = Classe
    template_name = 'cadastros/listas/classes.html'
    login_url = reverse_lazy('login')

class CampusList(LoginRequiredMixin, ListView):
    model = Campus
    template_name = 'cadastros/listas/campus.html'
    login_url = reverse_lazy('login')

class ProgressaoList(LoginRequiredMixin, ListView):
    model = Progressao
    template_name = 'cadastros/listas/progressao.html'

class SituacaoList(ListView):
    model = Situacao
    template_name = 'cadastros/listas/situacao.html'

class ComprovanteList(ListView):
    model = Comprovante
    template_name = 'cadastros/listas/comprovante.html'

class ValidacaoList(ListView):
    model = Validacao
    template_name = 'cadastros/listas/validacao.html'