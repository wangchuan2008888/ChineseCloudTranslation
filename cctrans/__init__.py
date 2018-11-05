from . import conf

from_lang = 'zh-CHS'
to_lang = 'en'
mode = 'youdao'
url = 'https://openapi.youdao.com/api'
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

"""
baidu - 不确定源和目的语言语种，可设置为auto
auto 自动检测
zh	中文
en	英语
yue	粤语
wyw	文言文
jp	日语
kor	韩语
fra	法语
spa	西班牙语
th	泰语
ara	阿拉伯语
ru	俄语
pt	葡萄牙语
de	德语
it	意大利语
el	希腊语
nl	荷兰语
pl	波兰语
bul	保加利亚语
est	爱沙尼亚语
dan	丹麦语
fin	芬兰语
cs	捷克语
rom	罗马尼亚语
slo	斯洛文尼亚语
swe	瑞典语
hu	匈牙利语
cht	繁体中文
vie	越南语
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


def set_url_sever(req_url):
    global url
    url = req_url


def translate(text):
    global mode
    global url
    if mode == 'youdao':
        from cctrans.core.youdao import translation
        return translation(text)
    else:
        from cctrans.core.baidu import translation
        return translation(text, url)
