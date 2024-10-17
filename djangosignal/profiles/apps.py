from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"

    def ready(self):
        # Import signals to ensure they are registered when the app is ready
        import profiles.signals
        import profiles.receivers
