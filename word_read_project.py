import pandas as pd
import numpy as np
import os
import time
import random

word_file_path = 'word/六级核心词汇表(EXCEL表格).xls'
data_log_path = 'data/data_log.csv'
# data_log = pd.read_csv(data_log_path)
words = pd.read_excel(word_file_path,header=0)
# print(len(words)+1)#求出一共多少列，从1开始算
# print(words.columns)#列索引名称
# print(words.index)#行索引名称

words_index = words.index

#函数功能：传入随机生成的单词索引，返回单词dataframe相关信息
def find_word(random_word_index,words):
	print(type(random_word_index))
	#根据随机单词的索引导出单词的相关信息
	random_words = words.loc[list(random_word_index)]
	# print(random_words)
	return random_words

#函数功能: 在进行random_80函数操作以后对word.csv进行同步记录,注意传进来的必须是列表的形式
def word_csv_log(random_words,time_stamp):
	word_path = 'data/word.csv'
	word_log = pd.read_csv(word_path,index_col=0)#读取单词日志文件,同时将索引设置为对应的时间
	for random_word in random_words:#将对应的随机抽取的单词5min,30min,12hour分别标记为1
		word_log.loc['time'][random_word] = time_stamp
		word_log.iloc[0:3][random_word][0] = 1
		word_log.iloc[0:3][random_word][1] = 1
		word_log.iloc[0:3][random_word][2] = 1

	word_log.to_csv(word_path)
	print('标记完成'.center(40,'='))


#函数功能:读取日志已经选择的单词索引内容返回列表
def data_log_read(data_log_path):
	data_logs = pd.read_csv(data_log_path)
	data_log_index = np.array(data_logs).tolist()
	return data_log_index

#函数功能：通过索引提取dataframe中的行，返回对应的dataframe数据方便生成csv文件
def random_80_word_to_csv(random_index,words):
	random_80_word_df = words.iloc[random_index,:]
	return random_80_word_df

#函数功能：随机从传入的单词索引列表中抽取80个词
def random_80_word(words_indexs,words):

	data_log_path = 'data/data_log.csv'
	# print(type(words_index))#显示传入索引格式
	try:
		data_log_index = data_log_read(data_log_path)#返回日志中的索引
		words_index = [i for  i in words_indexs if i not in data_log_index]
	except :
		words_index= list(words_indexs)
	random_word = random.sample(list(words_index),80)#同时记录被选中的索引数据
	print(len(random_word))
	random_words = find_word(random_word,words)[['单词']]
	random_words = np.array(random_words).tolist()#这里是列表嵌套的形式需要解套
	random_words = [i[0] for i in random_words]#将随机抽取的
	#time模块的使用还要考虑到后面everyday_word.csv文件命名的问题，文件名称中不能有特殊符号
	time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())#使用time模块以对应的年-月-日-小时-分钟的形式返回的数据为字符串
	every_day_word_path = 'every_day_word/'+str(time_stamp)+'.csv'
	random_80_word_df = random_80_word_to_csv(random_word,words)#在这一步调用函数同时生成对应random文件数据
	word_csv_log(random_words,time_stamp)

	print(type(random_80_word_df))
	random_80_word_df.to_csv(every_day_word_path)#生成80词csv文件
	data = {time_stamp: random_word}#用于data_log.csv路径不存在情况
	if os.path.exists(data_log_path):#将今天生成的随机单词存入日志csv文件中备用
		datas = pd.read_csv(data_log_path)
		datas.loc[:, str(time_stamp)] = pd.Series(random_word)
		# datas[time_stamp] = random_word #注意，由于日期的原因无法输入列索引相同的数据，dataframe本质有点像优化的数据库
		datas.to_csv(data_log_path,index=False)#注意这里的mode的设置，必须设置为覆盖模式
	else:
		datas = pd.DataFrame(data)
		datas.to_csv(data_log_path, index=False)


	return random_word,every_day_word_path#将随机索引的80个词返回




random_word_index,every_day_word_path = random_80_word(words_indexs=words_index,words= words)
# print(random_word_index)

random_words_df = find_word(random_word_index,words)#返回的依然是dataframe格式的数据
# print(type(random_words))#返回索引到的单词数据用于建立日期表
random_words = random_words_df[['单词']]#对列进行操作这里还是dataframe格式
random_words_lists = np.array(random_words).tolist()#注意这里的random_words_list每一个random_word都是单独的列表，迭代时需要[0]

for random_word in random_words_lists:
	print('今日随机单词'.center(80,'='))
	print(random_word[0])
#这里借助numpy将dataframe转换为list格式方便后面进行文件重组时间文件

#word_read_pro.py的最终目的就是提供80个随机单词，不具备判断能力,但是记录随机筛选的单词的索引

#在随后的返回函数中根据csv时间文件判断是否需要call_back
# random_words_lists = np.array(random_words).tolist()#注意这里的random_words_list每一个random_word都是单独的列表，迭代时需要[0]







