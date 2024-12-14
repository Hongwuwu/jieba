import jieba

sentence = "我来自北京信息科技大学"
seg_listy = jieba.cut(sentence, cut_all=True)
print('/'.join(seg_listy))

jieba.lcut(sentence)
print(jieba.lcut(sentence))


"""
练习

请将以下例句使用精确匹配模式进行分词，并将结果打印出来。  
例句："小明毕业于大连理工大学，后在美国佛罗里达大学深造"
> 提示：注意 cut 函数参数的设置
"""
sentence_Two = "小明毕业于大连理工大学，后在美国佛罗里达大学深造"
print(jieba.lcut(sentence_Two))


# 全部匹配模式
sentence_Three = "我来到北京航空航天大学"
seg_list = jieba.cut(sentence_Three, cut_all=True)
print('/'.join(seg_list))

seg_list = jieba.cut_for_search(sentence_Three)
print('/'.join(seg_list))

"""
练习：

请将以下例句使用搜索引擎模式进行分词，并将结果打印出来。  
例句："小明毕业于大连理工大学，后在美国佛罗里达大学深造"
"""
sentence_Two = "小明毕业于大连理工大学，后在美国佛罗里达大学深造"
seg_list = jieba.cut_for_search(sentence_Two)
print('/'.join(seg_list))

# 返回值
sentence_four = "我来到北京航空航天大学"
seg_gen = jieba.cut(sentence_four)
print('使用 jieba.cut() 方法，返回值的类型是: %s'%type(seg_gen))
seg_list = jieba.lcut(sentence_four)
print('使用 jieba.lcut() 方法，返回值的类型是: %s'%type(seg_list))


sent = '周大川是教务办主任也是大数据方面的工程师'
cut_list = jieba.cut(sent)
print('/'.join(cut_list))

sent = '周大川是教务办主任也是大数据方面的工程师'
jieba.add_word('周大川', freq=0)
cut_list = jieba.cut(sent)
print('/'.join(cut_list))

jieba.add_word('周大川', freq=2)
cut_list = jieba.cut(sent)
print('/'.join(cut_list))

"""
练习：
1. 请将‘大数据’添加到词典中，并打印分词结果。  
2. 请将‘大数据’从词典中删除，并打印分词结果。  
"""

#add
jieba.add_word('大数据', freq=2)
cut_list = jieba.cut(sent)
print('/'.join(cut_list))

#del
jieba.add_word('大数据', freq=0)
cut_list = jieba.cut(sent)
print('/'.join(cut_list))


"""
练习：
请保证‘台中’不被切分开  
例句：'[台中]正确应该不会被切开'
> 提示：尝试设置 freq 的大小，查看分词的结果
"""
sentt = '[台中]正确应该不会被切开'
jieba.add_word('台中', freq=69)
cut_list = jieba.cut(sentt)
print('/'.join(cut_list))

#######
#我自己测试阈值为69，但是用下面方法算的是70


"""
练习：
查看**周大川**和**大数据**的临界值
> 提示：使用方法 suggest_freq 同时 tune 设置为 False
"""

print('--'*20)
res = jieba.suggest_freq('大数据', tune=False)
print('词频的临界值:  %s'%res)

print('--'*20)
res = jieba.suggest_freq('周大川', tune=False)
print('词频的临界值:  %s'%res)



#del
sent = '周大川是教务办主任也是大数据方面的工程师'
# 删掉词语
jieba.suggest_freq('周大川')
jieba.suggest_freq('大数据')
# 查看分词结果
cut_list = jieba.cut(sent)
print('/'.join(cut_list))


file_path = './user_dict.txt'
jieba.load_userdict(file_path)
# 查看分词结果
cut_list = jieba.cut(sent)
print('/'.join(cut_list))

"""
练习：
请将教务办添加到词典文本中，然后重新分词查看结果。
> 例句： '周大川是教务办主任也是大数据方面的工程师'
"""

res = jieba.suggest_freq('教务办', tune=False)
print('词频的临界值:  %s'%res)


jieba.add_word('教务办', freq=0)
cut_list = jieba.cut(sent)
print('/'.join(cut_list))