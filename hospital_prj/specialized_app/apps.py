from django.apps import AppConfig


class SpecializedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'specialized_app'
