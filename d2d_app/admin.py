from django.contrib import admin
from d2d_app.models import *

admin.site.register([Customer, Package, Contract, Driver])
