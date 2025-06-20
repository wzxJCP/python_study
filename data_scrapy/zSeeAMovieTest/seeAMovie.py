﻿# -*- coding:utf-8 -*-

# url解析
from urllib import parse
import tkinter.messagebox as msgbox
import tkinter as tk
import webbrowser
import re

class APP:
	def __init__(self, width=500, height=300):
		self.w = width
		self.h = height
		self.title = '在线观看视频'
		self.root = tk.Tk(className=self.title)
		# 定义button控件上的文字
		self.url = tk.StringVar()

		# 定义选择哪个播放源
		self.v = tk.IntVar()

		# 默认为1
		self.v.set(1)

		# Frame空间
		frame_1 = tk.Frame(self.root)
		frame_2 = tk.Frame(self.root)
		frame_3 = tk.Frame(self.root)
		
		# Menu菜单
		menu = tk.Menu(self.root)                                                            
		self.root.config(menu=menu)
		moviemenu = tk.Menu(menu, tearoff=0)
		menu.add_cascade(label='菜单', menu=moviemenu)
		moviemenu.add_command(label='使用说明')
		moviemenu.add_command(label='关于作者')
		moviemenu.add_command(label='退出',command=self.root.quit)

		# 各大视频网站
		# moviemenu.add_command(label='腾讯视频', command=lambda: webbrowser.open('http://v.qq.com/'))
		# moviemenu.add_command(label='搜狐视频', command=lambda: webbrowser.open('http://tv.sohu.com/'))
		# moviemenu.add_command(label='芒果TV', command=lambda: webbrowser.open('http://www.mgtv.com/'))
		# moviemenu.add_command(label='爱奇艺', command=lambda: webbrowser.open('http://www.iqiyi.com/'))
		# moviemenu.add_command(label='PPTV', command=lambda: webbrowser.open('http://www.bilibili.com/'))
		# moviemenu.add_command(label='优酷', command=lambda: webbrowser.open('http://www.youku.com/'))
		# moviemenu.add_command(label='乐视', command=lambda: webbrowser.open('http://www.le.com/'))
		# moviemenu.add_command(label='土豆', command=lambda: webbrowser.open('http://www.tudou.com/'))
		# moviemenu.add_command(label='A站', command=lambda: webbrowser.open('http://www.acfun.tv/'))
		# moviemenu.add_command(label='B站', command=lambda: webbrowser.open('http://www.bilibili.com/'))

		# 控件内容设置
		group = tk.Label(frame_1, text='请选择视频解析方式：', padx=5, pady=5)
		tb1 = tk.Radiobutton(frame_1, text='通道一', variable=self.v, value=1, width=10, height=3)
		tb2 = tk.Radiobutton(frame_1,text='通道二', variable=self.v, value=2, width=10, height=3)
		tb3 = tk.Radiobutton(frame_1,text='通道三', variable=self.v, value=3, width=10, height=3)
		label1 = tk.Label(frame_2, text="请输入视频链接：")
		entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
		label2 = tk.Label(frame_2, text=" ")
		play = tk.Button(frame_2, text="播放", font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)
		label3 = tk.Label(frame_2, text=" ")
		# label_explain = tk.Label(frame_3, fg='red', font=('楷体', 18), text='\n注意：\n学习交流 \n禁止商用！')
		# label_warning = tk.Label(frame_3, fg='black', font=('楷体', 16),text='\n\n')

		# 控件布局
		frame_1.pack()
		frame_2.pack()
		frame_3.pack()
		group.grid(row=0, column=0)
		tb1.grid(row=0, column=1)
		tb2.grid(row=0, column=2)
		tb3.grid(row=0, column=3)
		label1.grid(row=0, column=0)
		entry.grid(row=0, column=1)
		label2.grid(row=0, column=2)
		play.grid(row=0, column=3,ipadx=10, ipady=10)
		label3.grid(row=0, column=4)
		# label_explain.grid(row=1, column=0)
		# label_warning.grid(row=2, column=0)

	"""
	函数说明:视频播放
	"""
	def video_play(self):
		# 视频解析网站地址
		# port_1 = 'https://jx.618g.com/?url='
		port_1 = 'https://jx.quanmingjiexi.com/?url='
		port_2 = 'http://www.wmxz.wang/video.php?url='
		port_3 = 'http://www.ckmov.vip/api.php?url='

		# 正则表达是判定是否为合法链接
		if re.match(r'^https?:/{2}\w.+$', self.url.get()):
			if self.v.get() == 1:
				# 视频链接获取
				ip = self.url.get()
				# 视频链接加密
				ip = parse.quote_plus(ip)
				# 浏览器打开
				webbrowser.open(port_1 + self.url.get())
			elif self.v.get() == 2:
				# 链接获取
				ip = self.url.get()
				# 链接加密
				ip = parse.quote_plus(ip)
				# 获取time、key、url
				get_url = 'http://www.wmxz.wang/video.php?url=%s' % ip
				# 请求之后立刻打开
				webbrowser.open(get_url)
			elif self.v.get() == 3:
				# 链接获取
				ip = self.url.get()
				# 链接加密
				ip = parse.quote_plus(ip)
				# 获取time、key、url
				get_url = 'http://www.ckmov.vip/api.php?url=%s' % ip
				# 请求之后立刻打开
				webbrowser.open(get_url)

		else:
			msgbox.showerror(title='错误',message='视频链接地址无效，请重新输入！')

	"""
	函数说明:tkinter窗口居中
	"""
	def center(self):
		ws = self.root.winfo_screenwidth()
		hs = self.root.winfo_screenheight()
		x = int((ws / 2) - (self.w / 2))
		y = int((hs / 2) - (self.h / 2))
		self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

	"""
	函数说明:loop等待用户事件
	"""
	def loop(self):
		# 禁止修改窗口大小
		self.root.resizable(False, False)
		# 窗口居中
		self.center()
		self.root.mainloop()

if __name__ == '__main__':
	app = APP()			# 实例化APP对象
	print("\n启动成功！")
	app.loop()			# loop等待用户事件
	print("\n退出成功！")