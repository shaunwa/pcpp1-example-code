def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance

        if instance:
            return instance
        
        instance = cls(*args, **kwargs)
        return instance

    return wrapper

@singleton
class Settings:
    def __init__(self, notifications_enabled, ringtone, timezone):
        self.notifications_enabled = notifications_enabled
        self.ringtone = ringtone
        self.timezone = timezone

s1 = Settings(True, 'ding', 'EST')
s2 = Settings(False, 'sadfgsdffgsdfg', 'asfasdfasdf')

print(s1 is s2)