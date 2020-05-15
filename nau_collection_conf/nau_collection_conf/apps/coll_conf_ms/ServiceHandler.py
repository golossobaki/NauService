from .models import Service


class GetService(Service):
    Service.objects.filter(Name='naucrm')