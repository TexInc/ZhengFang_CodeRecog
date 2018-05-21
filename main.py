# -*- coding: utf-8 -*-
"""
Created on 2018/5/20 

@author: susmote
"""

import requests
from predict_func import verify


if __name__ == '__main__':
    the_url = 'http://125.221.35.100/CheckCode.aspx'
    the_model = 'model/SVC_Model_zf.pkl'
    captcha_list = list(verify(the_url, the_model))
    captcha_code = ''.join(captcha_list)
    print(captcha_code)
