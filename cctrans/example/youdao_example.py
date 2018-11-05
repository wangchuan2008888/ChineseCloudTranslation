import cctrans

cctrans.conf.youdao_app_id = ''
cctrans.conf.youdao_secret_key = ''
cctrans.set_trans_cloud('youdao')
text = "我想去奥森吃饭，可是我不知道怎么过去"
print(cctrans.translate(text))

