from configparser import ConfigParser
from importlib_resources import path

conf = ConfigParser()

with path("cctrans", 'configure.ini') as p:
    conf.read(str(p))

youdao_app_id = conf.get('youdao', 'app_id')
youdao_secret_key = conf.get('youdao', 'token')
