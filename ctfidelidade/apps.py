from django.apps import AppConfig


class CtfidelidadeConfig(AppConfig):
    name = 'ctfidelidade'

    def ready(self):
        import ctfidelidade.signals 