# coding:utf-8  #强制使用utf-8编码格式
import sys

reload(sys)

sys.setdefaultencoding('utf-8')
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
import time


#发送邮件函数
def mail(my_sender,my_user):
    ret = True
    try:
        msg = MIMEText('<html><head><meta charset="utf-8"><title>亲！值日了哦！</title></head>'+
            '<body><h1>亲！值日了哦！</h1><p>亲爱的同学，轮到你值日了哦～为了宿舍的清洁卫生，请扫地、拖地、倒垃圾～</p>'+
            '<p align="right">213网管</p>'+
            '</body></html>', 'html', 'utf-8')
        msg['From'] = formataddr(["[213宿舍值日提醒程序:)]", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([tmp[0], my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = tmp[0]+'同学轮到你值日~'  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP("smtp.126.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "邮箱授权码")  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 这句是关闭连接的意思
    except Exception:  # 如果try中的语句没有执行，则会执行下面的ret=False
        ret = False
    return ret


# 打开文件
fo = open("/etc/email.txt", "r+")
listEmail=[]
while True:
    i = 0
    line = fo.readline()
    if not line:
        break
    line = line.strip('\n')
    listEmail.append(line)
    i = i + 1
# 关闭文件
fo.close()

#divide name and email address
str = listEmail[i]
tmp = str.split()
print(tmp[0]);
print(tmp[1]);
#取出第一个元素 执行发送邮件函数
ret = mail("fangzr_test@126.com", tmp[1])
if ret:
    print("接受人："+tmp[1]+"时间："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"状态：ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到
else:
    print("接受人："+tmp[1]+"时间："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"状态：filed")  # 如果发送失败则会返回filed


#调换顺序写入文件

fo = open("/etc/email.txt", "w")
for i in range(len(listEmail)-1):
    fo.write(listEmail[i+1]+'\n')
fo.write(listEmail[0])
fo.close()

 

