from django.contrib import admin
from .models import Komiks, DodatkoweInfo, Ocena, Aktor

#admin.site.register(Komiks) --pokazanie wszystkiego

@admin.register(Komiks)
class KomiksAdmin(admin.ModelAdmin):
    #fields = ["tytul","opis"]  --pokazanie wybranych pól z modelu
    #exclude = ["opis"]         --pokazanie wszystkich pól poza "opis"
    list_display = ["tytul", "imdb_rating", "rok"] #wyswietlenie dodatkowych parametrow w liscie
    list_filter = ["rok", "imdb_rating"] #dodanie filtrów wyszukiwania
    search_fields = ["tytul", "opis"] #dodanie wyszukiwarki, ustalenie w czym ma szukac

admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)