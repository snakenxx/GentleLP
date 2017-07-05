# coding = big5
import requests 
from bs4 import BeautifulSoup
import os
import re


FileExtensionList = ['.xlsx','.doc','.pdf','.txt']

for dirPath, dirNames, fileNames in os.walk("C:\\Users\\snaken\\Documents\\001 產品企劃\\"):
	for f in fileNames:
		if os.path.splitext(f)[-1] in FileExtensionList:
			s = re.sub("[\s+-\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",os.path.splitext(f)[0])
			for i in range(1,len(s)-3):
				if s[i:i+3].isnumeric() and not(s[i-1].isnumeric()):
					print(s[i-3:i+3])
			

No = input("please input the no:  ")
url = No
html = requests.get(url).text

with open('sss.txt','w', encoding = 'utf-8') as fp:
	fp.write(html)

sp = BeautifulSoup(html,'html.parser')
print(sp.title.text)
## 再來就解資料而已 
## 