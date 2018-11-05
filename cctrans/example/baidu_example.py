import cctrans
from cctrans import translate

cctrans.set_from_lang('auto')
cctrans.set_to_lang('auto')
cctrans.set_trans_cloud('baidu')
cctrans.set_url_sever('http://api.fanyi.baidu.com/api/trans/vip/translate')
cctrans.conf.baidu_app_id = ''
cctrans.conf.baidu_secret_key = ''
text = 'apple'
fanyi = translate(text)
print(fanyi)
