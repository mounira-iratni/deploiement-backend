from .base import *

# Clé secrète pour le développement. NE PAS UTILISER EN PRODUCTION.
SECRET_KEY = 'django-insecure-votre-cle-de-developpement-ici'

# Activer le mode débogage pour le développement
DEBUG = True

# En développement, on peut autoriser toutes les origines
ALLOWED_HOSTS = ['*']

# Base de données pour le développement local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}