import unittest
from cctrans import translate
import cctrans


class TestYoudao(unittest.TestCase):

    def test_trans_ch_eng(self):
        cctrans.conf.youdao_app_id = ''
        cctrans.conf.youdao_secret_key = ''
        cctrans.set_trans_cloud('youdao')
        text = '我想去奥森吃饭，可是我不知道怎么过去'
        print(translate(text))

    def test_baidu_trans(self):
        cctrans.set_from_lang('auto')
        cctrans.set_to_lang('auto')
        cctrans.set_trans_cloud('baidu')
        cctrans.set_url_sever('https://fanyi-api.baidu.com/api/trans/vip/translate')
        cctrans.conf.baidu_app_id = ''
        cctrans.conf.baidu_secret_key = ''
        text = """我爱北京天安门"""
        print(translate(text))
