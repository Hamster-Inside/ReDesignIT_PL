from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]