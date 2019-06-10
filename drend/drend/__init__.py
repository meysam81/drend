import os


def get_env(key, value=None):
    env = os.environ.get(key)

    if env:
        return env

    elif not value:
        raise KeyError(f"{key} not set!")

    return value


ENV = get_env('ENV')

default = None

# sometimes we need to deal with the project like: python manage.py something
if ENV.casefold() == 'management':
    default = 1


MONGO_DATABASE = get_env('MONGO_DATABASE', default)
MONGO_USERNAME = get_env('MONGO_USERNAME', default)
MONGO_PASSWORD = get_env('MONGO_PASSWORD', default)
MONGO_HOST = get_env('MONGO_HOST', default)
MONGO_PORT = int(get_env('MONGO_PORT', default))
