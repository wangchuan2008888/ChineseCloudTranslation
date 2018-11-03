import cctrans

cctrans.conf.youdao_app_id = '50448a43d85cad93'
cctrans.conf.youdao_secret_key = '4ahJuOnkr5Q7JX74juY0UaeX6CRLnrJF'
cctrans.set_trans_cloud('youdao')
text = "我爱北京天安门"
print(cctrans.translate(text))
