from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Vendas


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
