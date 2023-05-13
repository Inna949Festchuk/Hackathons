from tqdm import tqdm
import psycopg2

import csv
# import translators as tr
# import requests

from pprint import pprint
# from tqdm import tqdm
# from fake_headers import Headers

# from bs4 import BeautifulSoup
# from fake_headers import Headers


# ПАРСИМ СТРАНИЧКУ ГУГЛПЕРЕВОДЧИКА (не доднлано)

# HOST = "https://translate.google.com"
# PARAMS = {
#     "hl":"auto",
#     "sl":"auto",
#     "tl":"ru",
#     "text":"yes",
#     "op":"translate"
# }        

# HOSTVACANCIES = f"{HOST}"
# HEADERS = Headers(browser="firefox", os="win").generate()

# response = requests.get(HOSTVACANCIES, params=PARAMS, headers=HEADERS)
# text = response.text

# soup = BeautifulSoup(text, features='html.parser')     
        
# tags_divs = soup.find_all("div", class_="OlSOob")

# pprint(tags_divs)

# # for tag_div in tags_divs:
# #     tag_div_span = tag_div.find("span", class_="ryNqvb")
# #     translete = tag_div_span.text
# #     pprint(translete)

## - - - - - - - Рабочий переводчик (число запросов ограниченно!)
# # trans_values = 'yes'
# # result = tr.translate_text(trans_values, translator='yandex', from_language='auto', to_language='ru')
# # print(result)

# ПЕРЕВОДЧИК
# out_list = []
# with open ("in_dataset/_cities.csv", "r", encoding = "utf-8") as in_data:
#     in_cities = csv.DictReader(in_data, delimiter = ";")
#     for citi in tqdm(in_cities):
#         result_ru = tr.translate_text(citi.get('title_ru'), translator='yandex', from_language='auto', to_language='ru') 
#         result_en = tr.translate_text(citi.get('title_ru'), translator='yandex', from_language='auto', to_language='en')
#         out_list.append([citi.get('title_ru'), result_ru, result_en])
#         # pprint(out_list) 

# with open ("out_cities.csv", "w", encoding = "utf-8") as out_data:
#     writer = csv.writer(out_data, delimiter=';', quoting=csv.QUOTE_ALL)
#     writer.writerows(out_list)

# pprint("ok!")

## - - - - - - - 
# out_list = []
# with open ("in_dataset/_cities.csv", "r", encoding = "utf-8") as in_data:
#     in_cities = csv.DictReader(in_data, delimiter = ";")
#     for citi in tqdm(in_cities):
#         out_list.append([citi.get('title_ru'), citi.get('title_en')])
#         # pprint(out_list) 

# with open ("out_cities.csv", "w", encoding = "utf-8") as out_data:
#     writer = csv.writer(out_data, delimiter=';', quoting=csv.QUOTE_ALL)
#     writer.writerows(out_list)

# pprint("ok!")


