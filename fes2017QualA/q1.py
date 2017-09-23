# -*- coding:utf-8 -*-
import re
s = input()
if re.findall('^YAKI',s):
    print("Yes")
else:
    print("No")
