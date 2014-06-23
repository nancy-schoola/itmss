# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
from stdimage import StdImageField


class Secao(models.Model):
    ALIGN = (
        ('right', 'Direita'),
        ('left', 'Esquerda'),
    )
    titulo = models.CharField(u'Título', max_length=250)
    menu = models.CharField(max_length=30)
    slug = models.SlugField()
    conteudo = HTMLField(u'Conteúdo')
    ordem = models.IntegerField(default=1)
    imagem = StdImageField(upload_to='imagens', blank=True, null=True, variations={
        'icone': (128, 128, True),
    })
    cor = models.CharField(max_length=30, default='#0ea4b8')
    alinhamento = models.CharField(max_length=20, choices=ALIGN)

    class Meta:
        verbose_name = u'Seção'
        verbose_name_plural = u'Seções'

    def __unicode__(self):
        return self.titulo


class Servico(models.Model):
    titulo = models.CharField(u'Título', max_length=250)
    slug = models.SlugField(primary_key=True)
    intro = HTMLField(u'Introdução', max_length=400)
    conteudo = HTMLField(u'Conteúdo')
    ordem = models.IntegerField(default=1)
    imagem = StdImageField(upload_to='imagens', blank=True, null=True, variations={
        'icone': (128, 128, True),
    })
    cor = models.CharField(max_length=30, default='#0ea4b8')

    class Meta:
        verbose_name = u'Serviço'

    def __unicode__(self):
        return self.titulo


class Contato(models.Model):
    titulo = models.CharField(u'Título', max_length=250)
    mapa = models.CharField(max_length=500)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    ordem = models.IntegerField(default=1)


class Portfolio(models.Model):
    imagem = StdImageField(upload_to='imagens', blank=True, null=True)
    titulo = models.CharField(u'Título', max_length=250)
    slug = models.SlugField(primary_key=True)
    texto = HTMLField(u'Texto')
    link = models.URLField()
    ordem = models.IntegerField(default=1)

    def __unicode__(self):
        return self.titulo


class Banner(models.Model):
    imagem = StdImageField(upload_to='imagens', variations={
        'slide': (1600, 560, True),
    })
    titulo = models.CharField(u'Título', max_length=250)
    texto = HTMLField(u'Texto')
    ordem = models.IntegerField(default=1)