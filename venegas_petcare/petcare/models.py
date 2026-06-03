from django.db import models

class Especies(models.Model):
    nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.nombre

class Mascotas(models.Model):
    nombre = models.ForeignKey(Especies, on_delete=models.PROTECT, related_name="mascotas")
    chip = models.CharField(max_length=120)
    peso_kg = models.IntegerField()
    edad = models.CharField(max_length=20, unique=True)
    estado_vacunada = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.nombre} ({self.chip})"