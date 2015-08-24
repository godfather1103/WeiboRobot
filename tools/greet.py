# -*- coding: utf-8 -*-
import random
from tools import monitor

#吐槽函数
def hello(hour):
	monitor_info = monitor.monitor_http()
	if hour == 23:
		return "こんばんは~~ご主人さま~"+monitor_info
	if hour == 100:
		return "ご主人様、ピクチャーを発送する微博に成功"+monitor_info
	if hour == 101:
		return "주인 보내기 웨이보 성공!"+monitor_info		
	else:
		#myfile = open('../../res/greet.txt','rU')
		myfile = open(GetSomeConfig()+'/res/greet.txt','rU')
		lines = {}
		lines = myfile.readlines()
		index = random.choice(range(len(lines) - 1))
		return lines[index]

def comment():
	myfile = open(GetSomeConfig()+'/res/comment.txt','rU')
	lines = {}
	lines = myfile.readlines()
	index = random.choice(range(len(lines) - 1))
	return lines[index]

#获取一些配置信息
def GetSomeConfig():
	fin = open('WorkPath.json','r')
	ConfigInfo = fin.read()
	js = eval(ConfigInfo)
	fin.close()
	return js['WorkPath']
