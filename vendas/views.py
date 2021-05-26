from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Vendas
from .models import ItemDoPedido
from .forms import ItemPedidoForm


class DashboardView(View):

    def dispatch(self, request, *args, **kwargs):   # executa verificações antes de executar a view
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado, usuario sem permissão de acesso')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {'media': Vendas.objects.media(),
                'media_desc': Vendas.objects.media_desc(),
                'min': Vendas.objects.min(),
                'max': Vendas.objects.max(),
                'cont': Vendas.objects.cont(),
                'cont_nfes': Vendas.objects.cont_nfes(),
                }
        return render(request, 'vendas/dashboard.html', data)


class NovoPedido(View):
    def get(self, request):
        return render(request, 'vendas/novo-pedido.html')

    def post(self, request):
        data = {}
        data['form_item'] = ItemPedidoForm()
        data['numero'] = request.POST['numero']
        data['desconto'] = float(request.POST['desconto'].replace(',', '.'))
        data['venda_id'] = request.POST['venda_id']

        if data['venda_id']:
            venda = Vendas.objects.get(id=data['venda_id'])
            venda.desconto = data['desconto']
            venda.numero = data['numero']
            venda.save()
        else:
            venda = Vendas.objects.create(
                numero=data['numero'], desconto=data['desconto'])

        itens = venda.itemdopedido_set.all()
        data['venda'] = venda
        data['itens'] = itens
        return render(
            request, 'vendas/novo-pedido.html', data)


class NovoItemPedido(View):
    def get(self, request, pk):
        pass

    def post(self, request, venda):
        data = {}
        item = ItemDoPedido.objects.create(
            produto_id=request.POST['produto_id'], quantidade=request.POST['quantidade'],
            desconto=request.POST['desconto'], venda_id=venda)

        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itemdopedido_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data)


class ListaVendas(View):
    def get(self, request):
        vendas = Vendas.objects.all()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas})


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        venda = Vendas.objects.get(id=venda)
        data['form_item'] = ItemPedidoForm()
        data['numero'] = venda.numero
        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        data['itens'] = venda.itemdopedido_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data)


class DeletePedido(View):
    def get(self, request, venda):
        venda = Vendas.objects.get(id=venda)
        return render(
            request, 'vendas/delete-pedido-confirm.html', {'venda': venda})

    def post(self, request, venda):
        venda = Vendas.objects.get(id=venda)
        venda.delete()
        return redirect('lista-vendas')


class DeleteItemPedido(View):
    def get(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        return render(
            request, 'vendas/delete-itempedido-confirm.html', {'item_pedido': item_pedido})

    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        venda_id = item_pedido.venda.id
        item_pedido.delete()
        return redirect('edit-pedido', venda=venda_id)