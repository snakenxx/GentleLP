# coding=big5
import re
InputString = "�o�O���զr��aaHdd056.jpg"
s = re.sub("[\s+-\.\!\/_,$%^*(+\"\']+|[+�X�X�I�A�C�H�B~@#�D%�K�K&*�]�^]+", "",InputString)

for i in range(0,len(s)-2):
	if s[i:i+3].isnumeric():
		print(s[i-3:i+3])