#-*-coding:utf-8-*-
'''
IPEngineer Main Program File
'''
'''
导入的模块大全：
tkinter:GUI实现
tkinter.messagebox:Win32API对话框模块
socket:网络API
pyperclip：键盘Win32API
'''
import tkinter.messagebox as messagebox
import tkinter
from socket import gethostbyname,gaierror
from pyperclip import copy
class StopFunction(Exception):
    def __init__(self,msg=''):
        self.msg=msg
    def __str__(self):
        return self.msg
def getip(hostname:str='www.baidu.com')->'str or Boolean':
    try:
        return gethostbyname(hostname)
    except gaierror:
        return False
'''
help(getip)
print(getip()
      )
print(getip('htffdf'))
'''
can_copy=''
root=tkinter.Tk()
root.title('IP获取器')
root.iconbitmap(default ='icons/icon.ico')
root.geometry('300x100')
ipbox=tkinter.Entry(root)
ipbox.pack()
def get_ip():
    from tkinter import END

    global ipbox,ipshow,can_copy
    ip_val=ipbox.get()
    if len(ip_val) <= 0:
        messagebox.showerror('错误','请输入网址')
        raise StopFunction('用户未输入URL')
    data=getip(ip_val)
    if data==False:
        messagebox.showerror('错误','网址错误')
        raise StopFunction('用户未输入正确的URL')
    ipshow.delete(0,END)
    ipshow.insert(0,data)
    messagebox.showinfo('信息','已经显示了！')
    can_copy=data
def copy_it():
    global can_copy
    if can_copy == '':
        messagebox.showerror('错误','未查看任何IP！')
        raise StopFunction('未查看任何IP！')
    copy(can_copy)
    messagebox.showinfo('信息','已复制！')
ipout=tkinter.Button(root,text='查看IP',command=get_ip)
ipout.pack()
ipshow=tkinter.Entry(root)
ipshow.pack()
copy_btn=tkinter.Button(root,text='复制IP',command=copy_it)
copy_btn.pack()
root.mainloop()

