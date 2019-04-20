from .models import *
from django import forms

class InsereRegistroForm(forms.ModelForm):

    class Meta:

        model = Registros

        fields = [
            'data',
            'servico',
            'cliente'
        ]
        exclude = [
            'status'
        ]