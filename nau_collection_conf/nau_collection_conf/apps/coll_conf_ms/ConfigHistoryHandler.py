from .models import ConfigHistory


class GetConfigHistory(ConfigHistory):
    ConfigHistory.objects.filter(ConfigId=1)
