import time
import datetime
import pandas as pd
import numpy as np
from  word_read_project import every_day_word_path
from mail_send_project import mail_send_fuc

#函数功能：负责time时间的相减,并分别返回时间间隔时间为1day 2day 4day 7day 15day 的路径列表
def read_log_remind():
	word_log_path = '/word_recording_project/data/word.csv'
	word_log = pd.read_csv(word_log_path,index_col=0)
	word_log = word_log.T
	word_log = word_log[word_log.time != '1111-11-11-11-11']  # 提取word.csv文件中time所有不等于‘1111-11-11-11-11’的模块
	#将矩阵转置方便使用index提取路径
	time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime()).split('-')
	log_times = np.array(word_log['time']).tolist()
	today = datetime.datetime(int(time_stamp[0]),
	                          int(time_stamp[1]),
	                          int(time_stamp[2]),
	                          int(time_stamp[3]),
	                          int(time_stamp[4]))
	#分别设置对应天数的路径列表
	day_1_path = []
	day_2_path = []
	day_4_path = []
	day_7_path = []
	day_15_path = []
	for log_time in log_times:
		log_timed = log_time.split('-')
		# print(log_timed)
		last_day = datetime.datetime(
			int(log_timed[0]),
			int(log_timed[1]),
			int(log_timed[2]),
			int(log_timed[3]),
			int(log_timed[4])
		)
		reduce = today - last_day
		#用于判断天数
		if reduce.days == 1:
			path  = '/word_recording_project/every_day_word/'+log_time+'.csv'
			day_1_path.append(path)
		elif reduce.days == 2:
			path = '/word_recording_project/every_day_word/' + log_time+'.csv'
			day_2_path.append(path)
		elif reduce.days == 4:
			path = '/word_recording_project/every_day_word/' + log_time+'.csv'
			day_4_path.append(path)
		elif reduce.days == 7:
			path = '/word_recording_project/every_day_word/' + log_time+'.csv'
			day_7_path.append(path)
		elif reduce.days == 15:
			path = '/word_recording_project/every_day_word/' + log_time+'.csv'
			day_15_path.append(path)
	#列表收集完路径后还需要去重
	day_1_path = list(set(day_1_path))
	day_2_path = list(set(day_2_path))
	day_4_path = list(set(day_4_path))
	day_7_path = list(set(day_7_path))
	day_15_path = list(set(day_15_path))


	return day_1_path,day_2_path,day_4_path,day_7_path,day_15_path

#负责当天的推进5 min 30 min 12小时
def today_word_count():
	today_path = every_day_word_path
	print('今日要推送的地址是： ',today_path)
	time_stamp = time.strftime("%Y-%m-%d", time.localtime())
	subject = '艾宾浩斯 '+time_stamp+' 第一次单词提醒'
	mail_send_fuc(today_path,subject)
	time.sleep(300)#5min提醒
	mail_send_fuc(today_path,subject)
	time.sleep(1500)#30min提醒
	mail_send_fuc(today_path,subject)
	time.sleep(41400)#12小时提醒
	mail_send_fuc(today_path,subject)














