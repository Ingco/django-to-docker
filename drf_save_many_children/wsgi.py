"""
WSGI config for drf_save_many_children project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

root_dir = Path(__file__).resolve().parents[1]
load_dotenv(root_dir / '.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_save_many_children.settings')

application = get_wsgi_application()
