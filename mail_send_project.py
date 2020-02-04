
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
#从word.csv文件传入文件everyday文件路径就可以直接发送邮件
# everyday_file_path = '2020-02-02.csv'

#函数功能：传入附件路径，邮件的主题发送邮件并返回发送状态

def mail_send_fuc(everyday_file_path,subject):

	message = MIMEMultipart()
	msg_from = '**************'  # 发送方邮箱地址。
	password = '**************'  # 发送方QQ邮箱授权码，不是QQ邮箱密码。
	msg_to = '**********'
	msg_to_1 = '***********'  # 收件人邮箱地址。

	message = MIMEMultipart()
	message['From'] = msg_from  # 发送者
	message['To'] = msg_to  # 接收者

	# 邮件标题
	message['Subject'] = Header(subject, 'utf-8')

	# 邮件正文内容
	message.attach(MIMEText('艾宾浩斯根据你的遗忘曲线提醒单词'.center(20,'+'), 'plain', 'utf-8'))

	#打开文件

	part = MIMEApplication(open(everyday_file_path, 'rb').read())
	part.add_header('Content-Disposition', 'attachment', filename=everyday_file_path)

	message.attach(part)#添加文件

	try:
		client = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
		print("连接到邮件服务器成功")

		client.login(msg_from, password)
		print("登录成功")
		client.sendmail(msg_from, msg_to, message.as_string())
		print("发送成功")
	except smtplib.SMTPException as e:
		print("发送邮件异常")
	finally:
		client.quit()

# mail_send_fuc(everyday_file_path)

