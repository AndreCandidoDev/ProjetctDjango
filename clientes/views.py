from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import Person, Documento
from produtos.models import Produto
from vendas.models import Vendas
from .forms import PersonForm

# =================== CBV ========================================
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


@login_required  # decorator que protege o acesso da função por login
def persons_list(request):
    termo_busca = request.GET.get('pesquisa', None)
    if termo_busca:
        persons = Person.objects.all()
        persons = persons.filter(first_name=termo_busca)
    else:
        persons = Person.objects.all()  # recebe todos os elementos da tabela (model) Person
    print(persons)
    mensagem = 'Teste para filter'
    zoeira = False
    return render(request, 'person.html', {'persons': persons, 'message': mensagem, 'zoeira': zoeira})


@login_required
def persons_new(request):
    # if not request.user.has_perm('clientes.add_Person'):  # verifica se o usuario possui permissao de adicionar
    #     return HttpResponse('Nao autorizado')
    if not request.user.is_superuser:
        return HttpResponse('Não autorizado')
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)  # na tabela (model) Person procura (pk) a query id
    print(person)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    # form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')
    # return render(request, 'person_delete_confirm.html', {'form': form})
    return render(request, 'person_delete_confirm.html', {'person': person})


# ===================  CBV ===========================================

class PersonList(LoginRequiredMixin, ListView):
    model = Person
    # template_name = 'algum_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        primeiro_acesso = self.request.session.get('primeiro_acesso', False)
        if not primeiro_acesso:
            context['message'] = 'seja bem vindo ao seu primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'voce ja acessou hoje'
        context['footer_message'] = timezone.now()
        context['warning_message'] = 'If you remove a client it will be removed forever!'
        return context


class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person

    # pega o documento da pessoa diretamente sem executar mais uma query
    # usar para foreign key e one to one
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Vendas.objects.filter(
            pessoa_id=self.object.id
        )
        return context


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    template_name_suffix = '_update_form'
    # success_url = '/clientes/person_list'
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):  # se o parametro success_url nao for passado, aurl eh retornada por essa funçao
        return reverse_lazy('person_list_cbv')


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('clientes.deletar_clientes', )
    model = Person
    success_url = reverse_lazy('person_list_cbv')

# ==================================================================================================================


class ProdutoBulk(View):
    def get(self, request):
        produtos = ['banana', 'maca', 'limao', 'laranja', 'pera', 'melancia']
        list_produtos = []
        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)
        Produto.objects.bulk_create(list_produtos)
        return HttpResponse('It works')
