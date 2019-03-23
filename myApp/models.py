from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    dt_nasc = models.DateField()

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    dt_nasc = models.DateField()
    salario = models.FloatField()

    def __str__(self):
        return self.nome