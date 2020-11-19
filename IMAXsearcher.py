import requests
import time
import telegram
import datetime

API_KEY = "API Key of your Telegram Bot" # Enter Info
bot = telegram.Bot(token = API_KEY)
chat_id = "Chat ID of your Telegram Bot" # Enter Info

url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200826" # Change 20200826 to your date


imax = False

def notify():
    bot.sendMessage(chat_id = chat_id, text="아이맥스 오픈")
    

n = 0
while not(imax):
    resp = requests.get(url)
    screen = "<span class='screentype'><span class='imax'>IMAX</span></span>"

    if screen in resp.text:
        imax = True
        notify()
    else:
        n+=1
        now = datetime.datetime.now()
        print("{}회 반복 {}".format(n, now))
        time.sleep(30)
