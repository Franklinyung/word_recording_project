import pandas as pd
import numpy as np
import random
file_name = '六级核心词汇表(EXCEL表格)'
word_file_path = '/word_recording_project/word/' + file_name+'.xls'
words = pd.read_excel(word_file_path,header=0)
words_index = words.index

words = words[['单词']]
print(len(np.array(words).tolist()))
words = np.array(words).tolist()#将所有单词转换为列索引，行索引转换为天数
print(len(words))
datas = {}
A = 0
for word in words :
	datas[word[0]] = {
			"5min":0,
			"30min":0,
			'12hour':0,
			'day1':0,
			'day2':0,
			'day4':0,
			'day7':0,
			'day15':0,
			'time':'1111-11-11-11-11'
			}
	A +=1
words_df = pd.DataFrame(data=datas)
print(words_df)
words_df.to_csv('/word_recording_project/data/word.csv')
# print(words_df)




