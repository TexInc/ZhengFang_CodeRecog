# -*- coding: utf-8 -*-
"""
Created on 2018/5/20

@author: susmote
"""

kv_dict = {}
with open('../right_code.txt') as f:
    for value in f:
        value = value.strip()
        for i in value:
            kv_dict.setdefault(i, 0)
            kv_dict[i] += 1
print(kv_dict.keys())
print(len(kv_dict))

