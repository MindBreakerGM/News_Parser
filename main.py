import time
import pytz
import requests
from config import *
from lxml import html
from datetime import datetime

class Parser:
    def __init__(self) -> None:
        self.time_sending  = "10:00"
        self.politic_url = "https://www.m24.ru/rubrics/politics"
        self.city_url = "https://www.m24.ru/rubrics/city"
        self.society_url = "https://www.m24.ru/rubrics/society"
    def get_news(self) -> str:
        def get_data(self, category: str) -> str:
            data_dict = {
                'politic':html.fromstring(requests.get(self.politic_url).content),
                'city':html.fromstring(requests.get(self.city_url).content),
                'society':html.fromstring(requests.get(self.society_url).content),
            }
            post_data = ""
            for link in range(20):
                news_data = data_dict[category].xpath(f"/html/body/div[1]/div[5]/div/div/div[1]/div/div[2]/ul/li[{link}]/p/a/text()")
                if news_data:
                    post_data += "—" + news_data[1].replace("\n", " ").replace("\t", "").strip(" ") + "." + "\n"

            return post_data

        return NEWS_POST.format(get_data(self, "politic"),get_data(self, "society"),get_data(self, "city"))

class Bot:
    def __init__(self) -> None:
        self.token = TELEGRAM_BOT_TOKEN
        self.chat_id = CHAT_ID
    def send_news(self, message) -> None:
        r = requests.get(f'https://api.telegram.org/bot{self.token}/SendMessage?text={message}&chat_id={self.chat_id}')
        print("Success!") if r.status_code else print(f"Error!\n{r.text}")

if __name__ == '__main__':
    while True:
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
        parser_class = Parser()
        minute = moscow_time.minute
        if int(moscow_time.minute) < 10:
            minute = f'0{moscow_time.minute}'
        if str(moscow_time.hour) + ":" + str(minute) == parser_class.time_sending:
            bot_class = Bot()
            data = parser_class.get_news()
            bot_class.send_news(data)
            time.sleep(120)
