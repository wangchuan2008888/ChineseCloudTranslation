from . import conf

from_lang = 'zh-CHS'
to_lang = 'en'
mode = 'youdao'

"""
youdao
==============================
中文	zh-CHS
日文	ja
英文	EN
韩文	ko
法文	fr
俄文	ru
葡萄牙文	pt
西班牙文	es
越南文	vi
德文	de
阿拉伯文	ar
印尼文	id
"""


def get_lang():
    return from_lang, to_lang


def set_from_lang(lang):
    global from_lang
    from_lang = lang


def set_to_lang(lang):
    global to_lang
    to_lang = lang


def set_trans_cloud(cloud):
    global mode
    mode = cloud


def translate(text):
    global mode
    if mode == 'youdao':
        from cctrans.core.youdao import translation
    else:
        return None
    return translation(text)
