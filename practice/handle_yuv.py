#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import re
import os

# with...as 自动调用close()方法
with open('ipc_yuv_list.txt',encoding='ascii',errors='ignore') as f:
    cont = [line.strip() for line in f.readlines() if line.strip()]

print(cont)

idx = 0
while idx < len(cont) :
    oneline = cont[idx].split('.')
    cmd = "calc_psnr -i ./yuv/" + oneline[0] + "_qp40_weightp0.yuv " \
          + "-w 1920 -h 1080 " \
          + " -o ~/work/ipc_yuv/" + cont[idx]
    print(cmd)
    os.system(cmd)
    idx = idx + 1


#m = re.search("bitrate", all_the_text)
#print(m.group())

'''
pattern = re.compile("rc_en .*: .*")
m = pattern.findall(all_the_text)
print(m)

m = pattern.sub("rc_en : 1", all_the_text)
print(m)
'''

'''
a = 800; b = 957
while a < b :
    c = "hevc_config_parm_" + str(a)
    if all_the_text.find(c) == -1 : 
       print(c)

    a += 1
'''
