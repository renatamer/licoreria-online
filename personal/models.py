from django.db import models

PRIORIDAD = [
("B","Baja"),
("M", "Media"), 
("A","Alta"),
]

class Question(models.Model):
	titulo = models.CharField(max_length=60)
	pregunta = models.TextField(max_length=400)
	prioridad = models.CharField(max_length=1, choices=PRIORIDAD)

def __str__ (self):
	return self.titulo

	class Meta:
		"""docstring for Meta"""
		verbose_nombre = "Pregunta"
		verbose_nombre_plural = "Las Preguntas"
			
