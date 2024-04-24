from django.db import models

class DodatkoweInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Drama'),
    }

    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)

class Komiks(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True,blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True,blank=True)
    plakat = models.ImageField(upload_to="Plakaty", null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return  self.tytul_rok()
    def tytul_rok(self):
        return "{} ({})".format(self.tytul, self.rok)

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    komiks = models.ForeignKey(Komiks, on_delete=models.CASCADE)

class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    komiksy = models.ManyToManyField(Komiks)