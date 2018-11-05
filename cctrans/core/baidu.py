import random
import hashlib
import requests

from cctrans import conf
import cctrans


def _sign(app_key, secret_key, text):
    salt = random.randint(32768, 65536)
    sign = app_key + text + str(salt) + secret_key
    return hashlib.md5(sign.encode('utf8')).hexdigest(), salt


def _request_data(url, app_key, text, salt, sign, from_lang='en', to_lang='zh'):
    """
    :rtype: object
    """

    return "{url}?appid={app_key}&q={text}&from={from_lang}&to={to_lang}&salt={salt}&sign={sign}".format(
        **locals()
    )


def translation(text, url):
    app_key = conf.baidu_app_id
    secret_key = conf.baidu_secret_key
    sign, salt = _sign(app_key, secret_key, text)
    data = _request_data(url=url,
                         app_key=app_key,
                         text=text,
                         salt=salt,
                         sign=sign,
                         from_lang=cctrans.from_lang,
                         to_lang=cctrans.to_lang)
    resp = requests.get(data).json()
    if resp.get('trans_result'):
        trans_result = resp['trans_result']
        trans_result = [trans_content['dst'] for trans_content in trans_result]
        return trans_result
    else:
        return None

