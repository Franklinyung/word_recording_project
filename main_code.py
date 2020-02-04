import pandas as pd
import numpy as np
import os
import time
import random
from every_day_count_pro import *

#总的执行函数包括写入word.csv日志的功能

if __name__ == '__main__':
	day_1_paths, day_2_paths, day_4_paths, day_7_paths, day_15_paths = read_log_remind()
	today_word_count()
	time.sleep(3600)
	#1小时后再复习昨天的知识
	if len(day_1_paths) != False:
		for day_1_path in day_1_paths:
			subject = '1 天前的单词复习'.center(20,'=')
			mail_send_fuc(day_1_path,subject)

	time.sleep(900)

	if len(day_2_paths) != False:
		for day_2_path in day_2_paths:
			subject = '2 天前的单词复习'.center(20,'=')
			mail_send_fuc(day_2_path,subject)

	time.sleep(900)

	if len(day_4_paths) != False:
		for day_4_path in day_4_paths:
			subject = '4 天前的单词复习'.center(20,'=')
			mail_send_fuc(day_4_path,subject)

	time.sleep(900)

	if len(day_7_paths) != False:
		for day_7_path in day_7_paths:
			subject = '4 天前的单词复习'.center(20,'=')
			mail_send_fuc(day_7_path,subject)

	time.sleep(900)

	if len(day_15_paths) != False:
		for day_15_path in day_15_paths:
			subject = '15 天前的单词复习'.center(20,'=')
			mail_send_fuc(day_15_path,subject)













