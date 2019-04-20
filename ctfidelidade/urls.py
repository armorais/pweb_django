from django.conf.urls import url
from django.urls import path, include
from ctfidelidade.views import *
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'ctfidelidade'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('registro/cadastrar', RegistroCreateView.as_view(), name="cadastra_registro"),
    path('registros/', RegistrosListView.as_view(), name="lista_registros"),
    url(r'^busca/$', busca, name='busca_registros'),
#   	url(r'^registros_fw/',RegistrosList.as_view(),name='home'),
#    url(r'^registro_fw/(?P<cpf>[\w\-]+)/$',RegistroDetail.as_view(),name='home2')
]

urlpatterns = format_suffix_patterns(urlpatterns)