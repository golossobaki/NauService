from django.contrib import admin

from .models import Service, Config, ConfigHistory


admin.site.register(Service)
admin.site.register(Config)
admin.site.register(ConfigHistory)