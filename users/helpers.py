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
    host_addr = socket.gethostname()

    return jwt.decode(token, settings.SECRET_KEY, audience=host_addr,
                      issuer=host_addr)


def jwt_encode_handler(payload):
    return jwt.encode(payload, settings.SECRET_KEY)


def jwt_get_user_id_from_payload_handler(payload):
    return payload.get('uid')


def jwt_get_username_from_payload_handler(payload):
    return payload.get('sub')

"""
import time
import asyncio
import aiohttp
async def get_token(url, method, session, **kwargs):
    resp = await session.request(method=method, url=url, **kwargs)
    resp.raise_for_status()
    await resp.text()
    return resp.status != 200
async def main(url, method, repeats=10, **kwargs):
    async with aiohttp.ClientSession() as sess:
        tasks = [asyncio.create_task(get_token(url, method, sess, **kwargs)
) for _ in range(repeats)]
        t1 = time.perf_counter()
        res = await asyncio.gather(*tasks, return_exceptions=True)
        t2 = time.perf_counter() - t1
        l = len([r for r in res if r])
        print(f'took {t2} seconds handling {repeats}. errors: {l}')
        return 
_ = asyncio.run(main('http://localhost/users/1/', 'GET', headers={
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjEsInN1YiI6Im1leXNhbSIsImV4cCI6MTU1OTY3MzQyOSwiaWF0IjoxNTU5NjY5ODI5LCJuYmYiOjE1NTk2Njk4MjksImlzcyI6ImRyZW5kLW1zLWRyZW5kIiwiYXVkIjoiZHJlbmQtbXMtZHJlbmQifQ.kbiYTYrH7GJICu95PO5hmSzFHjEiHKBSoHUvYhGnMlQ'}, repeats=100))
"""