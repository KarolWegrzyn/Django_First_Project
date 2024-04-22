from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Komiks
from .forms import KomiksForm
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def wszystkie_komiksy(request): #dodanie metody zwracajacej widok (zwraca wszystkie rekordy z bazy)
    wszystkie = Komiks.objects.all() #pobranie wszystkich obiektow z bazy (ORM)
    return render(request, 'Komiksy.html', {'komiksy': wszystkie}) #zwrocenie strony html z template
@login_required
def nowy_komiks(request):
    form = KomiksForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_komiksy)

    return render(request,'komiks_form.html',{'form':form, 'nowy': True})
@login_required
def edytuj_komiks(request, id):     #parametr id pochodzi z urls
    #komiks = Komiks.objects.get(id)    pierwszy sposób
    komiks = get_object_or_404(Komiks, pk=id) #READ - pobranie rekordu z bazy w celu edycji
    form = KomiksForm(request.POST or None, request.FILES or None, instance=komiks)

    if form.is_valid(): #sprawdza poprawność danych
        form.save()
        return redirect(wszystkie_komiksy)

    return render(request,'komiks_form.html',{'form':form, 'nowy': False})

@login_required
def usun_komiks(request,id):
    komiks = get_object_or_404(Komiks, pk=id) #READ - pobranie rekordu z bazy w celu edycji

    if request.method =="POST":
        komiks.delete()
        return redirect(wszystkie_komiksy)

    return render(request,'potwierdz.html',{'komiks':komiks})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Przekierowanie na stronę po zalogowaniu.
            return redirect('wszystkie_komiksy')
        else:
            # Komunikat o błędnych danych logowania.
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # Przekierowanie na stronę po wylogowaniu.
    return redirect('login_url')
