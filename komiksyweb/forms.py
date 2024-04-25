from django.forms import ModelForm
from .models import Komiks, DodatkoweInfo, Ocena

class KomiksForm(ModelForm):
    class Meta:
        model = Komiks
        fields = ['tytul','rok','opis','premiera','imdb_rating','plakat']

class DodatkoweInfoForm(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ['czas_trwania','gatunek']

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']