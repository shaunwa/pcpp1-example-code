class DatabaseConnection:
    url = ''
    credentials = ''

    def __init__(self, url):
        self.url = url

    @classmethod
    def to_url(cls, url):
        cls.url = url
        return cls

    @classmethod
    def with_credentials(cls, credentials):
        cls.credentials = credentials
        return cls

    @classmethod
    def connect(cls):
        print(f'Connecting to {cls.url} with credentials {cls.credentials}...')
        new_instance = cls(cls.url)
        return new_instance

db = DatabaseConnection.to_url('google.com').with_credentials('Abc123').connect()