from d2d import settings
from django.core.management import setup_environ
setup_environ(settings)
from d2d_app.models import *

Package.objects.all.delete()
Delivery.objects.all.delete()
Contract.objects.all.delete()

