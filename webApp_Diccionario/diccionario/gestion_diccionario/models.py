from django.db import models

class Entradas(models.Model):
    Tipos_Palabras = models.TextChoices('TipoPalabra', 'Sustantivo Adjetivo Determinante Pronombre Verbo Adverbio Preposiciones Conjuncion')

    palabra=models.CharField(max_length=30)
    tipo_palabra=models.CharField(choices=Tipos_Palabras.choices, max_length=15)
    definiciones=models.CharField(max_length=200)

    def __str__(self):
        return "%s; %s" % (self.tipo_palabra, self.definiciones)
