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
    '''
    
    conn = psycopg2.connect(database='Cities', user='postgres', password='Atoer949')
    
    heder = get_heder()
    with conn.cursor() as cursor:

        try:
            for el in tqdm(get_list()):
                cursor.execute(f"INSERT INTO {table}({heder[0]}, {heder[1]}, {heder[2]}, {heder[3]}, {heder[4]}, {heder[5]}),"
                               f"{heder[6]}, {heder[7]}, {heder[8]}, {heder[9]}, {heder[10]}, {heder[11]},"
                               f"{heder[12]}, {heder[13]}, {heder[14]}, {heder[15]}, {heder[16]}, {heder[17]},"
                               f"{heder[18]}, {heder[19]}, {heder[20]}, {heder[21]}, {heder[22]}, {heder[23]},"
                               f"{heder[24]}, {heder[25]}, {heder[26]}, {heder[27]}, {heder[28]}, {heder[29]},"
                               f"{heder[30]}, {heder[31]}, {heder[32]}, {heder[33]}, {heder[34]}, {heder[35]},"
                               f"{heder[36]}, {heder[37]}, {heder[38]}, {heder[39]}, {heder[40]}, {heder[41]},"
                               f"{heder[42]}, {heder[43]}, {heder[44]}, {heder[45]})"
                               f"VALUES('{el[0]}', '{el[1]}', '{el[2]}', {el[3]}', '{el[4]}', '{el[5]}', {el[6]}', '{el[7]}',"
                               f"'{el[8]}', '{el[9]}', '{el[10]}', {el[11]}', '{el[12]}', '{el[13]}', {el[14]}', '{el[15]}',"
                               f"'{el[16]}', '{el[17]}', '{el[18]}', {el[19]}', '{el[20]}', '{el[21]}', {el[22]}', '{el[23]}',"
                               f"'{el[24]}', '{el[25]}', '{el[26]}', {el[27]}', '{el[28]}', '{el[29]}', {el[30]}', '{el[31]}',"
                               f"'{el[32]}', '{el[33]}', '{el[34]}', {el[35]}', '{el[36]}', '{el[37]}', {el[38]}', '{el[39]}',"
                               f"'{el[40]}', '{el[41]}', '{el[42]}', {el[43]}', '{el[44]}', '{el[45]}');"
                               )
                conn.commit()
                    
        except psycopg2.IntegrityError:
            print("(")
            None


def main():
    insert_db("_cities")


if __name__ == '__main__':
    main()