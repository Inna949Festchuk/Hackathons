import csv
from tqdm import tqdm
import psycopg2
# Для установки драйвера смени путь PATH=$PATH:/Applications/Postgres.app/Contents/Versions/12/bin/ pip install psycopg2

def get_heder():
    with open ("in_dataset/_cities.csv", "r", encoding = "utf-8") as in_data:
        in_cities = iter(csv.reader(in_data, delimiter = ";"))
        return next(in_cities)


def get_list():
    heder = get_heder()
    with open ("in_dataset/_cities.csv", "r", encoding = "utf-8") as in_data:
        in_cities = csv.DictReader(in_data, delimiter = ";")
        for citi in in_cities:
            yield [citi.get(f"{heder[i]}") for i in range(45)]


def insert_db(table):
    '''Функция обработки запроса для заполнения таблицы базы данных
    table - имя таблицы
    field - имя поля
    value - значения поля'''
    
    conn = psycopg2.connect(database='Cities', user='postgres', password='Atoer949')
    
    heder = get_heder()
    with conn.cursor() as cursor:

        try:
            for el in tqdm(get_list()):
                cursor.execute(f"INSERT INTO {table}({heder[0]}, {heder[1]}, {heder[2]}) VALUES('{el[0]}', '{el[1]}', '{el[2]}');")
                conn.commit()
                    
        except psycopg2.IntegrityError:
            print("(")
            None


def main():
    insert_db("_cities")


if __name__ == '__main__':
    main()