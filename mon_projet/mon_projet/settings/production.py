
import os
import dj_database_url
from .base import *

# Charger la clé secrète depuis les variables d'environnement
SECRET_KEY = os.environ.get('SECRET_KEY')

# Désactiver le mode débogage en production
DEBUG = False

# Charger les domaines autorisés depuis les variables d'environnement
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Configuration de la base de données de production via une URL
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=True
    )
}

# Configuration de WhiteNoise pour le stockage des fichiers statiques
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuration CORS plus restrictive pour la production
# On lit les origines autorisées depuis une variable d'environnement
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')