from django.conf.urls import url
from django.urls import path, include
from clientes_ms.views import *
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^clientes/',ClientesList.as_view(),name='home'),
    url(r'^cliente/(?P<cpf>[\w\-]+)/$',ClientesDetail.as_view(),name='home2')
]

urlpatterns = format_suffix_patterns(urlpatterns)