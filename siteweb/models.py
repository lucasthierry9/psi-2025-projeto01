from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=7)
    numero = models.IntegerField()
    posicao = models.CharField(max_length=50)
    local_nascimento = models.CharField(max_length=100)
    altura = models.CharField(max_length=10)
    gols = models.IntegerField()
    assists = models.IntegerField()
    imagem = models.ImageField(upload_to="jogadores/")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Jogadores"

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    data = models.CharField(max_length=50, blank=True)
    categoria = models.CharField(max_length=50, blank=True)
    texto = models.TextField()
    imagem = models.ImageField(upload_to="noticias/")

    def __str__(self):
        return self.titulo
    
class Sobre(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Elementos do Sobre"

class Jogo(models.Model):
    campeonato = models.CharField(max_length=50)
    rodada = models.CharField(max_length=50)
    estadio = models.CharField(max_length=50)
    data_hora = models.CharField(max_length=50)
    logo_casa = models.ImageField(upload_to="logos/")
    logo_fora = models.ImageField(upload_to="logos/")

    def __str__(self):
        return self.campeonato

class Informacao(models.Model):
    titulo = models.CharField(max_length=50)
    paragrafo = models.TextField()
    imagem = models.ImageField(upload_to="historia/")

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Informações"

