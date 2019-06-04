import datetime
import socket


from jose import jwt
from rest_framework_jwt.settings import api_settings as drf_settings
from django.conf import settings


def jwt_payload_handler(user):

    now = datetime.datetime.now()
    host_addr = socket.gethostname()
    return {
        'uid': user.id,
        'sub': user.username,
        'exp': now + drf_settings.JWT_EXPIRATION_DELTA,
        'iat': now,
        'nbf': now,
        'iss': host_addr,
        'aud': host_addr,
    }


def jwt_decode_handler(token):
    return jwt.decode(token, settings.SECRET_KEY, audience=socket.gethostname(),
                      issuer=socket.gethostname())


def jwt_encode_handler(payload):
    return jwt.encode(payload, settings.SECRET_KEY)


def jwt_get_user_id_from_payload_handler(payload):
    return payload.get('uid')


def jwt_get_username_from_payload_handler(payload):
    return payload.get('sub')


