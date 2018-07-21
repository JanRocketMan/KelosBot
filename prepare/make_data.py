import sir_liba ## uor library depends on vk_api
#import vk_api
import pandas as ps
import time

#PARSE VK

parser = sir_liba.VkParse('VK_LOGIN', 'VK_TOKEN')
parser.cleangrouptable()
for cat in ['Игры и киберспорт','Наука и технологии','Новости','Развлечения','Культура и искусство','Спорт']:
    parser.makegrouptable(cat, alpha=0.4)

i = 0
while i <= 1200:
    print("offset ", i)
    try:
        parser.scrapposts(filename='all_NEW', offset=i, total_count=1000)
        i += 100
    except:
        time.sleep(15*60)
        continue

#CLEAR DATAFRAME

eda = sir_liba.EdaMaker('all_posts.csv', text_series='text')
eda.cleantext()
eda.save(arg_name="edaed_posts.csv")

#Read sir_liba.help() for more info...
