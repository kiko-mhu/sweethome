#coding=gbk
from collections import OrderedDict
import codecs

#所有文件确保是utf-8编码，如果不是，请转码。
ipath = "绝代双娇.txt"
with codecs.open(ipath,'r','UTF-8') as file_object:
	contents = file_object.read()

dictc= {}
dictc_copy={}
dictc_sorted=OrderedDict()
for c in contents:
	if c == '…' or c == "’" or c == "‘" or c == '：' or c == '，' or c == '。' or c == '！' or c == '？' or c == ' ' or c == '、' or c == '\r' or c == '\n' or c == '（' or c == '）' or c == '《' or c == '》' or c == '“' or c == '”':
		continue
	exist = False
	for cc in dictc.keys():
		if c == cc:
			dictc[c]=dictc[c]+1
			exist = True
			break
	if exist != True:
		#暂时性的手动去掉这些标点符号
			dictc[c]=1

for key2 , value2 in dictc.items():
	dictc_copy[key2]=value2

max_value = 0
while dictc_copy:
	for key3 , value3 in dictc.items():
		if dictc[key3] >= max_value:
			exist2 = False
			if key3 not in dictc_sorted.keys():
				max_value = dictc[key3]
				max_key = key3
	dictc_sorted[max_key]=max_value
	del dictc_copy[max_key]
	max_value = 0

with codecs.open('绝代双娇_分析结果.txt','w','UTF-8') as file_object:
	for key , value in dictc_sorted.items():
		file_object.write("key : "+key+"    value : "+ str(value)+"\n")

print( ipath + "分析完毕！")
