# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_data
import qiniu.config

#需要填写你的 Access Key 和 Secret Key
access_key = 'jiKlNJc1Z46e_-rwnQieD7gmXYtj_SG7oGAMtgYn'
secret_key = 'pLznjB_LKcswS1WjcTaWP6l2J56tIFYMogEjlWjp'
def upload_file(ak,sk,file_data):
    #构建鉴权对象
    q = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = 'bnxydx01'

    #上传后保存的文件名
    key = None

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    #要上传文件的本地路径
    # localfile = './media/imgs/bbb.jpg'

    # ret, info = put_file_v2(token, key, version='v2')
    ret,info = put_data(token,key,file_data)
    return ret.get('key')
s = f"./media/imgs/touxiang.jpg"
if __name__ == '__main__':
    with open(r'F:\jdango_pro\django_protest\media\imgs\3d321615759b5c6337af61c8535bfa6.jpg','rb') as f:
        file_data = f.read()
        upload_file(access_key,secret_key,file_data)