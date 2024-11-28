from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transactions'

    def ready(self):
        from firebase_admin import credentials, initialize_app
        from django.conf import settings
        from . import signals

        cred = credentials.Certificate(settings.FIREBASE_CREDENTIAL_PATH)
        initialize_app(cred)
        return super().ready()

