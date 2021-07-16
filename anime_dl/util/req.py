"""
    Simple urllib3 wrapper
"""
import urllib3
import json
from ..info import text as version, name as app_name
POOL = urllib3.PoolManager()


def get(url, headers: dict = {}, args: dict = {}):
    """
      urllib3 GET
    """
    headers['User-Agent'] = f"{app_name}/{version}"

    r = POOL.request(
        'GET',
        "%s%s" % (url, '?' + urllib3.request.urlencode(args)
                  if len(args) > 0 else ''),
        headers=headers)
    return r.data.decode('utf-8')


def post(url, headers: dict = {}, args: dict = {}, body: dict = {}):
    """
      urllib3 POST
    """
    headers['Content-Type'] = 'application/json;charset=utf-8'
    headers['User-Agent'] = f"{app_name}/{version}"

    r = POOL.request(
        'POST',
        "%s%s" % (url, '?' + urllib3.request.urlencode(args)
                  if len(args) > 0 else ''),
        headers=headers,
        body=json.dumps(body).encode('utf-8') if len(body) else None)
    return r.data.decode('utf-8')

# vim: ft=python ts=4 noet
