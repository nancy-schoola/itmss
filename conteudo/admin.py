from django.contrib import admin
from conteudo.models import Secao, Servico, Contato, Portfolio, Banner


class SecaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ordem',)
    list_editable = ('ordem',)
    prepopulated_fields = {'slug': ('titulo',)}


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ordem',)
    list_editable = ('ordem',)
    prepopulated_fields = {'slug': ('titulo',)}


class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ordem',)
    list_editable = ('ordem',)


admin.site.register(Secao, SecaoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Contato)
admin.site.register(Portfolio)
admin.site.register(Banner, BannerAdmin)