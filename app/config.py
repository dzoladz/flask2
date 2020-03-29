import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hAX74iIVt5VwFNQltWnaZ3sdwBK5rJ89JwzYKit8mQ6sRJXV1H'