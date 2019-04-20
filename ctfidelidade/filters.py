from django.contrib.auth.models import User
from .models import Registros
import django_filters

class ClienteFilter(django_filters.FilterSet):
    class Meta:
        model = Registros
        fields = ['cliente', ]