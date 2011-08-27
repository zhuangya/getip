import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'getip.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
