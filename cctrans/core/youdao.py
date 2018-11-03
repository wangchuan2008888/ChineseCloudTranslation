import random
import hashlib
import requests

from cctrans import conf
import cctrans

url = 'https://openapi.youdao.com/api'


def _sign(app_key, secret_key, text):
    salt = random.randint(1, 65536)
    sign = app_key + text + str(salt) + secret_key

    return hashlib.md5(sign.encode('utf8')).hexdigest(), salt


def _request_data(url, app_key, text, salt, sign, from_lang='en', to_lang='zh'):
    """

    :rtype: object
    """
    return "{url}?appKey={app_key}&q={text}&from={from_lang}&to={to_lang}&salt={salt}&sign={sign}".format(
        **locals()
    )


def translation(text):
    app_key = conf.youdao_app_id
    secret_key = conf.youdao_secret_key
    sign, salt = _sign(app_key, secret_key, text)
    data = _request_data(url=url,
                         app_key=app_key,
                         text=text,
                         salt=salt,
                         sign=sign,
                         from_lang=cctrans.from_lang,
                         to_lang=cctrans.to_lang)
    resp = requests.get(data).json()
    if int(resp['errorCode']) == 0:
        return resp['translation']
    else:
        return None
