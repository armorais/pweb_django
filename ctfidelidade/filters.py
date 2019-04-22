from django.contrib.auth.models import User
from .models import Registros, Premios
import django_filters

class ClienteRegistroFilter(django_filters.FilterSet):
    class Meta:
        model = Registros
        fields = ['cliente', ]

class ClientePremioFilter(django_filters.FilterSet):
    class Meta:
        model = Premios
        fields = ['cliente', ]