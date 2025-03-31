import datetime

class logger:
    def __init__(self, module_name):
        self.module_name = module_name
    
    def __call__(self, *args, level = 'INFO'):
        args = [str(arg) for arg in args]
        print(f'[AVFMS] [{datetime.datetime.now()}] [{level}] {self.module_name} ' + ' '.join(args))

    def info(self, *args):
        self(*args)

    def error(self, *args):
        self(*args, level = 'ERROR')

    def warning(self, *args):
        self(*args, level = 'WARNING')
    
    def debug(self, *args):
        self(*args, level = 'DEBUG')
