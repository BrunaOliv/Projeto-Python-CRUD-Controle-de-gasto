from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Transacao, Categoria
from django.urls import reverse_lazy
from django.db.models import Sum

# Create your views here.

class IndexView(TemplateView):
    template_name = "modelo.html"

class TransacaoCreat(CreateView):
    model = Transacao
    fields = ['data', 'descricao', 'valor', 'categoria', 'observacoes']
    template_name = 'form.html'
    success_url = reverse_lazy('list_transacao')

class TransacaoUpdate(UpdateView):
    model = Transacao
    fields = ['data', 'descricao', 'valor', 'categoria', 'observacoes']
    template_name = 'form.html'
    success_url = reverse_lazy('list_transacao') 

class TransacaoDelete(DeleteView):
    model = Transacao
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('list_transacao')    

class TransacaoList(ListView):
    model = Transacao
    template_name = 'list.html'
    data = Transacao.objects.all().aggregate(sum=Sum('valor'))
    print(data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data) 

def Sum(request):
    _sum = Transacao.objects.all().aggregate(sum=Sum('valor'))
    print(_sum)
    return render(request, 'list.html', {"sum":_sum})