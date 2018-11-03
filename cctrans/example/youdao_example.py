import cctrans

cctrans.conf.youdao_app_id = ''
cctrans.conf.youdao_secret_key = ''
cctrans.set_trans_cloud('youdao')
text = "我想去奥森吃饭，可是我不知道怎么过去"
print(cctrans.translate(text))

cctrans.set_from_lang('auto')
cctrans.set_to_lang('auto')
cctrans.set_trans_cloud('baidu')

cctrans.conf.baidu_app_id = ''
cctrans.conf.baidu_secret_key = ''

text = """
without any luck.

I guess I could always try to use base64 before encoding, but I'd like to leave that as a "last resource"... I was hoping for a more "elegant" way of doing this.

Has anyone encountered the same problems? Any hint will be appreciated. Thank you in advance.
"""
print(cctrans.translate(text))