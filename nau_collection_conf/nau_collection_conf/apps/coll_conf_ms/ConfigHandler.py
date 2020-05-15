from .models import Config


class GetConfig(Config):
    Config.objects.get(FileName='mv-event-dispatcher.properties')


test_config = GetConfig()
print(test_config)
