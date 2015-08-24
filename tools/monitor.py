# -*- coding: utf-8 -*-
import urllib2
import os
import platform
import time
#from tools import greet
#监视某个网站的http链接
def monitor_http():
	try:
		urllib2.urlopen('https://github.com/godfather1103')
		return "https://github.com/godfather1103 神经连接正常。"
	except:
		return 'https://github.com/godfather1103 网站打不开了！'

#监视cpu温度
def monitor_cpu_temp():
    temp =  float(os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C\n",""))
    if temp > 50:
        return "cpu的体温 %.2f°C...热死了~~" % (temp)
    return "cpu的体温 %.2f°C...." % (temp)

#获取运行时间
def monitor_runtime():
    uptime = {}
    if platform.system()=='Windows':
     	all_sec = BootTime()
    elif platform.system()=='Linux':
    	f = open("/proc/uptime")
    	con = f.read().split()
     	f.close()
     	uptime['Free rate'] = float(con[1]) / float(con[0])
     	all_sec = float(con[0])
    else:
    	boottime = 0 	
    
    
    MINUTE,HOUR,DAY = 60,3600,86400
    uptime['day'] = int(all_sec / DAY )
    uptime['hour'] = int((all_sec % DAY) / HOUR)
    uptime['minute'] = int((all_sec % HOUR) / MINUTE)
    uptime['second'] = int(all_sec % MINUTE)
    uptime['allminute']= int(all_sec / MINUTE)
    runtime = '服务器已经工作了%d天%d小时%d分。' % (uptime['day'], uptime['hour'], uptime['minute'])
    return runtime
    
#计算程序运行时间
def BootTime():
	fin = open('WorkPath.json','r')
	ConfigInfo = fin.read()
	js = eval(ConfigInfo)
	fin.close()
	sytime = (time.localtime())
	year = sytime.tm_year-js['Year']
	mon = sytime.tm_mon-js['Month']
	day = sytime.tm_mday-js['Day']
	hour = sytime.tm_hour-js['Hour']
	min = sytime.tm_min-js['Min']
	sec = sytime.tm_sec-js['Sec']
	total = year*365*24*3600+mon*30*24*3600+day*24*3600+hour*3600+min*60+sec
	
	return total

#print os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C\n","")    
#print os.popen('systeminfo').readline()
#print monitor_cpu_temp()