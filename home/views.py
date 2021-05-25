from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic.base import TemplateView


# arquitetura FBV (functions based views)
def home(request):
    return render(request, 'home.html')


def polices(request):
    return render(request, 'polices.html')


def services_term(request):
    return render(request, 'services_terms.html')


def exclusion(request):
    return render(request, 'exclusion.html')


def Logout(request):
    logout(request)
    return redirect('home')


# arquitetura CBV (class based views)
class HomePageView(TemplateView):
    template_name = "home3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variavel_teste'] = 'Ola isso eh so um teste'
        return context


# =============== Exemplo view generica ===============================
from django.http import HttpResponse
from django.views import View


class MyView(View):

    def get(self, request, *args, **kwargs):
        # return HttpResponse('Hello, World!')
        # return render(request, 'home3.html')  # pode tbm retornar template
        response = render_to_response('home3.html')
        response.set_cookie('color', 'blue', max_age=1000)
        mycookie = request.COOKIES.get('color')
        print(mycookie)
        return response

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')
