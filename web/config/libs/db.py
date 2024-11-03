import os

from dotenv import load_dotenv

load_dotenv()

DB_ENGINE = {
    'SQLITE3': 'django.db.backends.sqlite3',
    'MySQL': 'django.db.backends.mysql',
    'PostgreSQL': 'django.db.backends.postgresql'
}

DATABASE = os.environ.get('DATABASE', default='SQLITE3')


def SETTING_DATABASE(path):
    if DATABASE == 'MySQL':
        return {'default': {
            'ENGINE': DB_ENGINE.get(DATABASE),
            'HOST': os.environ.get('DB_HOST', default='mariadb'),
            'PORT': os.environ.get('DB_PORT', default=3306),
            'NAME': os.environ.get('MYSQL_DATABASE', default='djradiocms'),
            'USER': os.environ.get('MYSQL_USER', default='djradiocmsuser'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD',
                                       default='djradiocmspass'),
        }}
    elif DATABASE == 'PostgreSQL':
        pass
    else:
        return {'default': {
            'ENGINE': DB_ENGINE.get(DATABASE),
            'NAME': path / 'db.sqlite3',
        }}
