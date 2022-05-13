from .base import *

secret_setting = json.loads(open(SECRET_SETTING_FILE).read())

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = secret_setting['DJANGO']['databases']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEST = True

ALLOWED_HOSTS = secret_setting['DJANGO']['allowed_hosts']
