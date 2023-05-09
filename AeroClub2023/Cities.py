import csv
from pprint import pprint
from tqdm import tqdm

out_list = []
with open ("in_dataset/_cities.csv", "r", encoding = "utf-8") as in_data:
    in_cities = csv.DictReader(in_data, delimiter = ";")
    for citi in tqdm(in_cities):
        out_list.append([citi.get('title_ru'), citi.get('title_en')])
        # pprint(out_list) 

with open ("out_cities.csv", "w", encoding = "utf-8") as out_data:
    writer = csv.writer(out_data, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerows(out_list)

pprint("ok!")
