from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import Person
from .forms import PersonForm


@login_required  # decorator que protege o acesso da função por login
def persons_list(request):
    persons = Person.objects.all()  # recebe todos os elementos da tabela (model) Person
    print(persons)
    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)  # na tabela (model) Person procura (pk) a query id
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
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
