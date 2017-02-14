# -*- coding:utf-8 -*-
import re
s = input()
l = "WBWBWWBWBWBW" * 3
scale = { 0:"Do", 2:"Re", 4:"Mi", 5:"Fa", 7:"So", 9:"La", 11:"Si" }
print(scale[l.index(s)])

