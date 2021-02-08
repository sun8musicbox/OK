


#import sentencepiece as spm




from ctypes import cdll
  
cur = cdll.LoadLibrary('/home/sentence/build/src/libsentencepiece.so')
cur.Load("/home/sentencepiece/sentencepiece.bpe.model") 

#a = cur.max(1, 2)
 
#print(a)







# 这是一个简单的python 程序
print("hello world!")

print("您好！")
print("这是最后一行")

