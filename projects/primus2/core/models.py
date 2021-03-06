from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_aluno = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)


class PlanoDeEstudo(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    professor = models.ForeignKey(User,
                                related_name='planos',
                                on_delete=models.CASCADE)
    is_publico = models.BooleanField(default=False)


    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    plano = models.ForeignKey(PlanoDeEstudo,
                              related_name='disciplinas',
                              on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Assunto(models.Model):
    disciplina = models.ForeignKey(Disciplina,
                                   related_name='assuntos',
                                   on_delete=models.CASCADE)
    nome = models.CharField(max_length=200,)
    descricao = models.TextField(blank=True)

    class Meta:
        unique_together = ('disciplina', 'nome')

    def __str__(self):
        return f'{self.disciplina.plano} - {self.disciplina} - {self.nome}'


class Atividade(models.Model):
    estudante = models.ForeignKey(User, related_name='estudantes',
                                  on_delete=models.DO_NOTHING)
    assunto = models.ForeignKey(Assunto,
                                related_name='atividades',
                                on_delete=models.CASCADE)
    criada = models.DateTimeField(auto_now_add=True)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    is_realizada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.assunto}'


class Anotacao(models.Model):
    atividade = models.ForeignKey(Atividade,
                                  related_name='anotacoes',
                                  on_delete=models.CASCADE)
    descricao = models.TextField(blank=True)