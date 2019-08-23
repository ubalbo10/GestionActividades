from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre=models.CharField(max_length=100)
    ciclo=models.IntegerField(blank=False)
    ingeniero=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    tema=models.CharField(max_length=100,blank=False)
    tipo=models.ForeignKey('Tipo',on_delete=models.CASCADE)
    materia=models.ForeignKey('Materia',on_delete=models.CASCADE)
    fecha=models.DateTimeField()
    horaIncio=models.TimeField()
    horaFin=models.TimeField()
    duracion=models.TimeField()
    terminado=models.BooleanField(default=False)
    comentario=models.TextField()

    def __str__(self):
        return "" + str(self.tema) + ", " + str(self.materia) + ""

    def duracion(self):
        return self.duracion==self.horaFin-self.horaInicio

class Tipo(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()

    def __str__(self):
        return self.nombre





