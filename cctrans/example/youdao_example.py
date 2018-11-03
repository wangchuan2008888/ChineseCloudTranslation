import cctrans

cctrans.conf.youdao_app_id = '<your_app_id>'
cctrans.conf.youdao_secret_key = '<your_secret_key>'
cctrans.set_trans_cloud('youdao')
text = "我爱北京天安门"
print(cctrans.translate(text))
