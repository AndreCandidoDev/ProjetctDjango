from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Produto
# Create your views here.


class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context


class ProdutoDetail(LoginRequiredMixin, DetailView):
    model = Produto


class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['descricao', 'preco']
    success_url = '/produtos/produto_list'


class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['descricao', 'preco']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


class ProdutoDelete(LoginRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('produto_list')
