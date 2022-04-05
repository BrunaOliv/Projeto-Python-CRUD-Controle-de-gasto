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
    template_name = "index.html"

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


def listagem(request):
    object_list = {}
    object_list = Transacao.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    categoria = request.GET.get('categoria')
    descricao = request.GET.get('descricao')
    print(categoria)
    if start_date and end_date:
       object_list = object_list.filter(data__range=[start_date, end_date])

    if categoria:
       object_list = object_list.filter(categoria=categoria)

    if descricao:
       object_list = object_list.filter(descricao__icontains=descricao)    

    _sum = object_list.aggregate(sum=Sum('valor'))
    context = {'object_list' : object_list, 'sum':_sum}
    return render(request, 'list.html', context)
