from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from conteudo.forms import ContactForm
from conteudo.models import Secao, Servico, Contato, Portfolio, Banner


class SiteMixin(View):
    def get_context_data(self, **kwargs):
        dados = super(SiteMixin, self).get_context_data(**kwargs)
        dados['secoes'] = Secao.objects.order_by('ordem')
        dados['servicos'] = Servico.objects.order_by('ordem')
        dados['contatos'] = Contato.objects.order_by('ordem')
        dados['clientes'] = Portfolio.objects.order_by('ordem')
        return dados


class Home(SiteMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        dados = super(Home, self).get_context_data(**kwargs)
        dados['slides'] = Banner.objects.order_by('ordem')
        dados['form'] = ContactForm(self.request.GET or None)
        return dados


class PortfolioList(SiteMixin, ListView):
    template_name = 'portifolio-list.html'
    context_object_name = 'portifolios'
    model = Portfolio


class PortifolioDetail(SiteMixin, DetailView):
    template_name = 'portifolio-detalhe.html'
    context_object_name = 'portfolio'
    model = Portfolio


class ServicoDetail(SiteMixin, DetailView):
    template_name = 'servico-detalhe.html'
    context_object_name = 'servico'
    model = Servico