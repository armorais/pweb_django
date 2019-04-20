from django.dispatch import receiver
from django.core.signals import post_save
from django.contrib.auth.models import User
from .models import Registros
