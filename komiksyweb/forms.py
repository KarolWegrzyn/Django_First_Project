from django.forms import ModelForm
from .models import Komiks

class KomiksForm(ModelForm):
    class Meta:
        model = Komiks
        fields = ['tytul','rok','opis','premiera','imdb_rating','plakat']