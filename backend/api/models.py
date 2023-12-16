from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CicleMenstrual(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    data_camp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.usuari + " - " + self.data_camp

class DiaMenstrual(models.Model):
    cicle = models.ForeignKey(CicleMenstrual, on_delete=models.CASCADE)
    dia = models.IntegerField()

    # Compreses
    compresa_poc_tacada = models.IntegerField()
    compresa_mitja_tacada = models.IntegerField()
    compresa_molt_tacada = models.IntegerField()
    compresa_coaguls = models.IntegerField()

    # Tampons
    tampo_poc_tacat = models.IntegerField()
    tampo_mitja_tacat = models.IntegerField()
    tampo_molt_tacat = models.IntegerField()
    tampo_coaguls = models.IntegerField()

    def __str__(self):
        return self.cicle.usuari + " - " + self.cicle.data_camp + " - " + self.dia

class EncuestaQOL(models.Model):
    mes_7_dies = models.BooleanField()
    mes_3_dies_abunda = models.BooleanField()
    regla_molesta = models.BooleanField()
    mancha_ropa = models.BooleanField()
    manchar_asiento = models.BooleanField()
    evitar_activitats = models.BooleanField()

    usuari = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuari