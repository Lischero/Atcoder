# -*- coding:utf-8 -*-
import re
S = input()
scale = ["Do", "#", "Re", "#", "Mi", "Fa", "#", "So", "La", "#", "Si", "#"]
flag = re.finditer(r"WW",S)
for tmp in flag:
    index = tmp.start()
    if index >= 4:
        break

print(scale[4-index])
