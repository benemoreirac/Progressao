from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Campo, Atividade, Status, Classe, Campus
from django.urls import reverse_lazy

# Create your views here.
class StatusCreate(CreateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class CampusCreate(CreateView):
    model = Campus
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class ClassesCreate(CreateView):
    model = Classe
    fields = ['nome', 'nível', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome','descricao']
    template_name ='cadastros/form.html'
    success_url = reverse_lazy('home')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')


###### UPDATE ######

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class StatusUpdate(UpdateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class CampusUpdate(UpdateView):
    model = Campus
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')

class ClassesUpdate(UpdateView):
    model = Classe
    fields = ['nome', 'nível', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')


###### DELETE ######

class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')

class StatusDelete(DeleteView):
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')

class CampusDelete(DeleteView):
    model = Campus    
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')

class ClassesDelete(DeleteView):
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('home')
