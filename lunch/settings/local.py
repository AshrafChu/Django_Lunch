from .base import *

SECRET_KEY ='cfuqbr@u-sey!s4!p08=$56q6t9d9$3e4)#fr&s2$xt*8+#jfo'
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname (BASE_DIR), 'db.sqlite3'),
    }
}




