class Database:
    log_level = 'SILENT'

    def connect(self, url):
        if self.__class__.log_level == 'VERBOSE':
            print(f'Connecting to {url}')

    def query(self, query_options):
        if self.__class__.log_level == 'VERBOSE':
            print(f'Making a query with options: {query_options}')
    
    def disconnect(self):
        if self.__class__.log_level == 'VERBOSE':
            print('Disconnecting from database')
        
    @classmethod
    def enable_verbose_logging_for_all(cls):
        cls.log_level = 'VERBOSE'

    @classmethod
    def disable_verbose_logging_for_all(cls):
        cls.log_level = 'SILENT'

db1 = Database()
db2 = Database()
db3 = Database()

db1.connect('google.com')
db1.query({})
db1.disconnect()

Database.enable_verbose_logging()

db2.connect('google.com')
db2.query({})
db2.disconnect()

Database.disable_verbose_logging()

db3.connect('google.com')
db3.query({})
db3.disconnect()