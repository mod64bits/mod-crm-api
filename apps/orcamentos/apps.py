from django.apps import AppConfig


class OrcamentosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orcamentos'
    
    def ready(self):
        import apps.orcamentos.signals
