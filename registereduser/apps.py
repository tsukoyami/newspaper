from django.apps import AppConfig


class RegistereduserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registereduser'


    def ready(self):
        import registereduser.signals
