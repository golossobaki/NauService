from django.http import HttpResponse
from .models import Service
import sh


def index(request):
    return HttpResponse("")


res = sh.ssh('root@192.168.0.202', 'ls / && ls /root')
print(res)
