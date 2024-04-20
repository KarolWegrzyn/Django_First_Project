from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Komiks
from .forms import KomiksForm
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGOUT_URL, request.path))
def wszystkie_komiksy(request): #dodanie metody zwracajacej widok (zwraca wszystkie rekordy z bazy)
    wszystkie = Komiks.objects.all() #pobranie wszystkich obiektow z bazy (ORM)
    return render(request, 'Komiksy.html', {'komiksy': wszystkie}) #zwrocenie strony html z template

def nowy_komiks(request):
    form = KomiksForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_komiksy)

    return render(request,'komiks_form.html',{'form':form})

def edytuj_komiks(request, id):     #parametr id pochodzi z urls
    #komiks = Komiks.objects.get(id)    pierwszy sposób
    komiks = get_object_or_404(Komiks, pk=id) #READ - pobranie rekordu z bazy w celu edycji
    form = KomiksForm(request.POST or None, request.FILES or None, instance=komiks)

    if form.is_valid(): #sprawdza poprawność danych
        form.save()
        return redirect(wszystkie_komiksy)

    return render(request,'komiks_form.html',{'form':form})

def usun_komiks(request,id):
    komiks = get_object_or_404(Komiks, pk=id) #READ - pobranie rekordu z bazy w celu edycji

    if request.method =="POST":
        komiks.delete()
        return redirect(wszystkie_komiksy)

    return render(request,'potwierdz.html',{'komiks':komiks})