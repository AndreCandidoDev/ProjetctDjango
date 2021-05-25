from django.contrib import admin
from .models import Vendas, ItemDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


class ItemPedidoStack(admin.StackedInline):
    model = ItemDoPedido
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    list_filter = ('pessoa__doc',)
    # raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa',)
                           # 'produtos')
    # list_display = ('id', 'pessoa', 'total', 'nfe_emitida')
    list_display = ('id', 'pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    # filter_vertical = ['produtos']
    # filter_horizontal = ['produtos']
    inlines = [ItemPedidoInline]
    # inlines = [ItemPedidoStack]

    def total(self, obj):
        return obj.calcular_total()

    total.short_description = 'Total'


admin.site.register(Vendas, VendaAdmin)
# admin.site.register(Produto, ProdutoAdmin)
admin.site.register(ItemDoPedido)