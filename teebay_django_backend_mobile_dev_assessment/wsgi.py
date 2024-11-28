"""
WSGI config for teebay_django_backend_mobile_dev_assessment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teebay_django_backend_mobile_dev_assessment.settings')

application = get_wsgi_application()
