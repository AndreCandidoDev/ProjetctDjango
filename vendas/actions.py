from django.http import HttpResponseNotFound


def nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseNotFound('<h1>Sem permissão</h1>')


def nfe_nao_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.remover_nfe'):
        queryset.update(nfe_emitida=False)
    else:
        return HttpResponseNotFound('<h1>Sem permissão</h1>')


nfe_emitida.short_description = "NF-e emitida"
nfe_nao_emitida.short_description = "NF-e nao emitida"



