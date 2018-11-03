import unittest
from cctrans import translate
import cctrans

class TestYoudao(unittest.TestCase):

    def test_trans_ch_eng(self):
        text = '我想去奥森吃饭，可是我不知道怎么过去'
        print(translate(text))

    def test_baidu_trans(self):
        cctrans.set_from_lang('auto')
        cctrans.set_to_lang('auto')
        cctrans.set_trans_cloud('baidu')
        text = '我想去奥森吃饭，可是我不知道怎么过去'
        print(translate(text))
