# -*- encoding: utf-8 -*-
'''
@File : p2_count_char.py
@Time : 2020/03/13 09:47:22
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
???????
'''

# here put the import lib

#??1
# sentence = "I can because i think i can"
# result = {word: sentence.split().count(word) for word in set(sentence.split())}
# print(result)

#??2
from collections import Counter
str = 'I can because i think i can'
counts = Counter(str.split())
print(counts)