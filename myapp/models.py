from django.db import models


class Persona(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        abstract = True


class Profesor(Persona):
    salario = models.FloatField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id', 'first_name', 'last_name'], name='primary_key_profesor'
            )
        ]

    def to_json(self):
        model_in_json = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'salario': self.salario
        }

        return model_in_json


class Salon(models.Model):
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()
    # idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, default=0)
    idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def to_json(self):
        model_in_json = {
            'aula': self.aula,
            'hora_entrada': str(self.hora_entrada),
            'idProfesor': self.idProfesor_id
        }

        return model_in_json


# Proxy de Modelo Salon
class OrderedSalon(Salon):
    class Meta:
        ordering = ['hora_entrada']
        proxy = True


class Alumno(Persona):
    idSalon = models.ForeignKey(Salon, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id', 'first_name', 'last_name'], name='primary_key_alumno'
            )
        ]

    def to_json(self):
        model_in_json = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'idSalon': self.idSalon_id
        }

        return model_in_json


# Proxy de Modelo Alumno
class OrderedAlumno(Alumno):
    class Meta:
        ordering = ['last_name']
        proxy = True


class Evaluacion(models.Model):
    hora_fecha = models.DateTimeField()
    curso = models.CharField(max_length=30)
    evaluador = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Examen_Final(Evaluacion):
    duracion = models.IntegerField()
    n_preguntas = models.IntegerField()
    puntaje_total = models.IntegerField()

    def puntaje_pregunta(self):
        return self.puntaje_total / self.n_preguntas

    def to_json(self):
        model_in_json = {
            'hora_fecha': str(self.hora_fecha),
            'curso': self.curso,
            'evaluador': self.evaluador,
            'duracion': self.duracion,
            'n_preguntas': self.n_preguntas,
            'puntaje_total': self.puntaje_total
        }

        return model_in_json


class Proyecto(Evaluacion):
    tema_proyecto = models.CharField(max_length=100)
    n_grupos = models.IntegerField()

    def to_json(self):
        model_in_json = {
            'hora_fecha': str(self.hora_fecha),
            'curso': self.curso,
            'evaluador': self.evaluador,
            'tema_proyecto': self.tema_proyecto,
            'n_grupos': self.n_grupos,
        }

        return model_in_json


class OrderedNameProyecto(Proyecto):
    class Meta:
        proxy = True
        ordering = ['tema_proyecto']
