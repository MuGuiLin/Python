# 安装插件
# pip install pyautogui
# pip install apscheduler

# 导入
import pyautogui as pg 
import pyperclip as pc 
from apscheduler.schedulers.blocking import BlockingScheduler 

# 操作间隔为1秒 
pg.PAUSE = 1 

name = '文件传输助手' 
text = '6868卡卡就发！' 

def main(msg):  
    # 打开微信  
    pg.hotkey('ctrl', 'alt', 'w') 

    # 搜索指定的人   
    pg.hotkey('ctrl', 'f') 
    pc.copy(name)  
    pg.hotkey('ctrl', 'v')  
    pg.press('enter')  

    # 发送消息  
    pc.copy(msg)  
    pg.hotkey('ctrl', 'v')  
    pg.press('enter')  

    # 隐藏微信  
    pg.hotkey('ctrl', 'alt', 'w')

main(text)
# if __name__ == '__main__':  
#     scheduler = BlockingScheduler() # 实例化一个调度器  
#     # scheduler.add_job(main, 'cron', hour = 10, minute = 30) # 添加任务 每天10:30 
#     scheduler.add_job(main, 'date', run_date='2021-8-23 10:30:00',  args=[text]) # 添加任务 指定时间，1次 
#     scheduler.start()