# -*- coding: utf-8 -*-
"""
Created on 2018/5/20 

@author: susmote
"""

import requests
from verify import verify

# 全局变量
captcha_url = 'http://125.221.35.100/CheckCode.aspx'


def get_codeimg(captcha_url):
    i = 51
    for i in range(200):
        i = int(i)
        i += 1
        session = requests.session()
        r = session.get(captcha_url)
        img_name = 'full_image/' + 'code_' + str(i) + '.jpg'
        with open(img_name, 'wb') as f:
            f.write(r.content)
        print(i)

if __name__ == '__main__':
    the_url = 'http://125.221.35.100/CheckCode.aspx'
    the_model = 'model/SVC_Model_zf.pkl'
    print(verify(the_url, the_model))
    print(verify(the_url, the_model, save=True))
