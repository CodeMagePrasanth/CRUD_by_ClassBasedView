"""
WSGI config for project35_CRUD_by_Class_based_view project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project35_CRUD_by_Class_based_view.settings')

application = get_wsgi_application()
