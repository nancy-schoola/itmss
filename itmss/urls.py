from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from conteudo.views import Home, PortfolioList, ServicoDetail, PortifolioDetail
from conteudo.views import Portfolio
import object_tools

admin.autodiscover()
object_tools.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),
    url(r'^portfolio/$', PortfolioList.as_view(), name='portfolio'),
    url(r'^portfolio/(?P<slug>[-_\w]+)/$', PortifolioDetail.as_view(), name='portfolio-detalhe'),
    url(r'^servicos/(?P<slug>[-_\w]+)/$', ServicoDetail.as_view(), name='servico-detalhe'),
    # url(r'^blog/', include('blog.urls')),
    (r'^object-tools/', include(object_tools.tools.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

