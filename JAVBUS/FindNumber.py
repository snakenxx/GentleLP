# coding=big5
import re
InputString = "這是測試字串aaHdd056.jpg"
s = re.sub("[\s+-\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",InputString)

for i in range(0,len(s)-2):
	if s[i:i+3].isnumeric():
		print(s[i-3:i+3])