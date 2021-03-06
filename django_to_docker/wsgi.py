"""
WSGI config for django_to_docker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

root_dir = Path(__file__).resolve().parents[1]
load_dotenv(root_dir / '.env')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_to_docker.settings')

application = get_wsgi_application()
