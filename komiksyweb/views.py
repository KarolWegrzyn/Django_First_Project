from django.shortcuts import render, get_object_or_404, redirect
from .models import Komiks, DodatkoweInfo, Ocena
from .forms import KomiksForm, DodatkoweInfoForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def wszystkie_komiksy(request): #dodanie metody zwracajacej widok (zwraca wszystkie rekordy z bazy)
    wszystkie = Komiks.objects.all() #pobranie wszystkich obiektow z bazy (ORM)
    return render(request, 'Komiksy.html', {'komiksy': wszystkie}) #zwrocenie strony html z template
@login_required
def nowy_komiks(request):
    form_komiks = KomiksForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)

    if all((form_komiks.is_valid(), form_dodatkowe.is_valid())):
        komiks = form_komiks.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        komiks.dodatkowe = dodatkowe
        komiks.save()
        return redirect(wszystkie_komiksy)

    return render(request,'komiks_form.html',{'form':form_komiks,'form_dodatkowe': form_dodatkowe,'nowy': True})
@login_required
def edytuj_komiks(request, id):     #parametr id pochodzi z urls
    #komiks = Komiks.objects.get(id)    pierwszy sposób
    komiks = get_object_or_404(Komiks, pk=id) #READ - pobranie rekordu z bazy w celu edycji
    oceny = Ocena.objects.filter(komiks=komiks)

    try:
        dodatkowe = DodatkoweInfo.objects.get(komiks=komiks.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None

    form_komiks = KomiksForm(request.POST or None, request.FILES or None, instance=komiks)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)

    if all((form_komiks.is_valid(), form_dodatkowe.is_valid())):
        komiks = form_komiks.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        komiks.dodatkowe = dodatkowe
        komiks.save()
        return redirect(wszystkie_komiksy)

    return render(request,'komiks_form.html',{'form':form_komiks,'form_dodatkowe': form_dodatkowe,'oceny': oceny, 'nowy': False})

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
