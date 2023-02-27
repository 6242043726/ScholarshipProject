from django.apps import AppConfig


class ScholarshipmanagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scholarshipmanager'

    def ready(self):
        import scholarshipmanager.signals
