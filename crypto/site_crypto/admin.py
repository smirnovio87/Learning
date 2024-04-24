from django.contrib import admin
from .models import Exchange, Assets, Deals


admin.site.register([Exchange, Assets, Deals])
