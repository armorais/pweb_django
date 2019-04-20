from django.contrib import admin

# Register your models here.
from .models import Premios
from .models import Registros
from .models import Servicos

admin.site.register(Premios)
admin.site.register(Registros)
admin.site.register(Servicos)