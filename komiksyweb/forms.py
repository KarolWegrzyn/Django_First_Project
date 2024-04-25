from django.forms import ModelForm
from .models import Komiks, DodatkoweInfo

class KomiksForm(ModelForm):
    class Meta:
        model = Komiks
        fields = ['tytul','rok','opis','premiera','imdb_rating','plakat']

class DodatkoweInfoForm(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ['czas_trwania','gatunek']