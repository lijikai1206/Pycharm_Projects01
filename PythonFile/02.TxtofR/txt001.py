# -*- coding:utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')
fp = open("resources.txt", "r")
sample = fp.readlines()

file=open("test.txt", "w")

for line in sample:
    sample_ = line.split('固定字符')
    print(sample_[n])
    file.write(sample_[n])
    file.write('\n')
