from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Campo, Atividade, Status, Classe, Campus
from django.urls import reverse_lazy
from django.views.generic.list import ListView 

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# Create your views here.
class StatusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class CampusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Campus
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class ClassesCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'nível', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

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

class CampusUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Campus
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class ClassesUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'nível', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')


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

class CampusDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Campus    
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')

class ClassesDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')


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

class CampusList(LoginRequiredMixin, ListView):
    model = Campus
    template_name = 'cadastros/listas/campus.html'
    login_url = reverse_lazy('login')

class ClasseList(LoginRequiredMixin, ListView):
    model = Classe
    template_name = 'cadastros/listas/classes.html'
    login_url = reverse_lazy('login')