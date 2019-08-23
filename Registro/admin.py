from django.contrib import admin
from .models import *

class ActividadAdmin(admin.ModelAdmin):
    #se ocupa para ver que campos son visibles de cada objeto
    list_display = ['tema','materia','tipo','fecha','horaFin']
    #fields se ocupa para ver que campos se rellenaran en cada creacion fields=['','']
    #para realizar busquedas solo se puede de un campo
    search_fields = ['tema']
    list_filter = ['fecha','materia','terminado']
    #list_filter=['materia']


# Register your models here.
admin.site.register(Materia)
admin.site.register(Actividad,ActividadAdmin)
admin.site.register(Tipo)