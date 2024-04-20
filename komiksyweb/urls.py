from django.urls import path #dodanie pliku urls.py w celu podzialu adresów urls
from komiksyweb.views import wszystkie_komiksy, nowy_komiks, edytuj_komiks, usun_komiks

urlpatterns = [
    path('wszystkie/', wszystkie_komiksy, name = "wszystkie_komiksy"), #dodanie sciezki do projektu
    path('nowy/', nowy_komiks, name = "nowy_komiks"),
    path('edytuj/<int:id>/', edytuj_komiks, name = "edytuj_komiks"), #przesłanie do funkcji parametru id
    path('usun/<int:id>/', usun_komiks, name = "usun_komiks")
]
