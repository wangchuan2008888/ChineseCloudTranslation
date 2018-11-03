import unittest
from cctrans import translate


class TestYoudao(unittest.TestCase):

    def test_trans_ch_eng(self):
        text = '我爱北京天安门'
        print(translate(text))
