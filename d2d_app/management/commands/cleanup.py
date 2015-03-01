from django.core.management.base import BaseCommand, CommandError
from d2d_app.models import *

class Command(BaseCommand):
    help = 'Cleans up all deliveries and packages from database'

    def handle(self, *args, **options):
        Delivery.objects.all().delete() 
        Contract.objects.all().delete() 
        Package.objects.all().delete() 
