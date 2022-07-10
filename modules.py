import pymysql

# pobieranie zdjęcia głównego


def get_img_link(product_number):
    dic = {
        'pc-2-0001': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-2/pc-2-0001.jpg",
        'pc-2-0002': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-2/pc-2-0002.jpg",
        'pc-2-0003': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-2/pc-2-0003.jpg",
        'pc-2-0004': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-2/pc-2-0004.jpg",
        'pc-2-0005': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-2/pc-2-0005.jpg",
        'pc-3-0001': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-3/pc-3-0001.jpg",
        'pc-3-0002': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-3/pc-3-0002.jpg",
        'pc-3-0003': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-3/pc-3-0003.jpg",
        'pc-3-0004': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-3/pc-3-0004.jpg",
        'pc-3-0005': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-3/pc-3-0005.jpg",
        'pc-4-0001': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-4/pc-4-0001.jpg",
        'pc-4-0002': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-4/pc-4-0002.jpg",
        'pc-4-0003': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-4/pc-4-0003.jpg",
        'pc-4-0004': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-4/pc-4-0004.jpg",
        'pc-4-0005': "../STANDARD_OFFER_GENERATOR/grafiki/packing tables/pc-4/pc-4-0005.jpg",

    }
    return dic[product_number]

# Składowe stołu


def get_accesories(product_number):
    dic = {
        'pc-2-0001': ['ec-2-0001'],
        'pc-2-0002': ['ec-2-0001', 'P-WP-1660-001', 'P-F2-002', 'P-PK2-001-5'],
        'pc-2-0003': ['ec-2-0001', 'P-PD2-001', 'P-WP-1660-001', 'P-PK2-002', 'P-PK2-001-5'],
        'pc-2-0004': ['ec-2-0001', 'P-WP-1660-001', 'P-PK2-002', 'P-PK2-001-5', 'P-F2-002'],
        'pc-2-0005': ['ec-2-0001', 'P-PD2-001', 'P-PW-002', 'P-PW-003', 'P-WP-1660-001', 'P-F2-002', 'P-V1-001', 'P-PK2-001-5'],
        'pc-3-0001': ['ec-3-0001'],
        'pc-3-0002': ['ec-3-0001', 'P-WP-1660-001', 'P-F3-002', 'P-PK3-001-6'],
        'pc-3-0003': ['ec-3-0001', 'P-PD3-001', 'P-WP-1660-001', 'P-PK3-002', 'P-PK3-001-6'],
        'pc-3-0004': ['ec-3-0001', 'P-WP-1660-001', 'P-PK3-002', 'P-PK3-001-6', 'P-F3-002'],
        'pc-3-0005': ['ec-3-0001', 'P-PD3-001', 'P-PW-002', 'P-PW-003', 'P-WP-1660-001', 'P-F3-002', 'P-V1-001', 'P-PK3-001-6'],
        'pc-4-0001': ['ec-4-0001'],
        'pc-4-0002': ['ec-4-0001', 'P-WP-1660-001', 'P-F4-002', 'P-PK4-001-7'],
        'pc-4-0003': ['ec-4-0001', 'P-PD4-001', 'P-WP-1660-001', 'P-PK4-002', 'P-PK4-001-7'],
        'pc-4-0004': ['ec-4-0001', 'P-WP-1660-001', 'P-PK4-002', 'P-PK4-001-7', 'P-F4-002'],
        'pc-4-0005': ['ec-4-0001', 'P-PD4-001', 'P-PW-002', 'P-PW-003', 'P-WP-1660-001', 'P-F4-002', 'P-V1-001', 'P-PK4-001-7'],

    }
    return dic[product_number]


# określanie wielkości blatu
def get_top_size(product_number):
    if int(product_number[3]) == 2:
        return "../STANDARD_OFFER_GENERATOR/grafiki/blat 1200.jpg"
    elif int(product_number[3]) == 3:
        return "../STANDARD_OFFER_GENERATOR/grafiki/blat 1600.jpg"
    elif int(product_number[3]) == 4:
        return "../STANDARD_OFFER_GENERATOR/grafiki/blat 2000.jpg"

# Licznie rabatu


def discount(quantity):
    if quantity < 20:
        return quantity
    else:
        return 20

# liczenie ceny po rabacie


def dis_price(price, discount):
    return price-price*(discount/100)

# Zapytania do bazy o dane produktu


class QueryContainer:

    def __init__(self, kod_produktu):
        self.name = f"SELECT nazwa FROM cennik WHERE kod_produktu LIKE '%{kod_produktu}%'"
        self.price = f"SELECT cena FROM cennik WHERE kod_produktu LIKE '%{kod_produktu}%'"
        self.describe = f"SELECT opis FROM cennik WHERE kod_produktu LIKE '%{kod_produktu}%'"

    def db(self, query):
        try:
            with pymysql.connect(
                host='host.lh.pl',
                user='serwerxxxxx',
                password='xxxxx',
                database='xxxxx',
            ) as connection:
                mycursor = connection.cursor()
                mycursor.execute(query)
                for x in mycursor:
                    return x[0]
        except ConnectionError:
            print("Check Internet Connection.")

# Pobieranie danych z bazy danych o kliencie


class Query:
    def __init__(self, data):
        self.get_id_by_name = f"SELECT id FROM lead WHERE kontakt LIKE '%{data}%'"
        self.get_name_by_id = f"SELECT kontakt FROM lead WHERE id LIKE '%{data}%'"
        self.get_company_name_by_id = f"SELECT dane_firmy FROM lead WHERE id LIKE '%{data}%'"
        self.get_tell_by_id = f"SELECT telefon FROM lead WHERE id LIKE '%{data}%'"
        self.get_price_by_code = f"SELECT cena FROM cennik WHERE kod_produktu LIKE '%{data}%'"
        self.get_price_by_name = f"SELECT cena FROM cennik WHERE nazwa LIKE '%{data}%'"
        self.get_tresc_zapytania_by_id = f"SELECT tresc_zapytania FROM lead WHERE id LIKE'%{data}%'"

    def db(self, query):
        try:
            with pymysql.connect(
                host='host.lh.pl',
                user='serwerxxxx',
                password='xxxxx',
                database='xxxxxx',
            ) as connection:
                mycursor = connection.cursor()
                mycursor.execute(query)
                for x in mycursor:
                    return x[0]
        except ConnectionError:
            print('Check Internet Connection.')

# liczenie całkowitej wartości zamówienia


def count_total(item):
    return sum(QueryContainer(kod_produktu).db(QueryContainer(kod_produktu).price) for kod_produktu in item)


# dodawanie kontenerów z informacjami o akcesoriach
containers = ['', '', '', '', '', '', '', '', '', '', '', '']


def add_container(item):
    counter = 0

    for kod_produktu in item:

        query = QueryContainer(kod_produktu)
        nazwa_produktu = query.db(query.name)
        opis_produktu = query.db(query.describe)
        cena_produktu = query.db(query.price)
        img_produktu = f"../STANDARD_OFFER_GENERATOR/grafiki/zestawienie elementów/{kod_produktu}.png"

        element = f"""
        <div class="container">
            <div class="elementy">
                <img class="img_height"  src="{img_produktu}" alt="{nazwa_produktu}">
            </div>
            <span class="opis">
                <p style="font-size: 20px;"><b>{nazwa_produktu}</b></p>
                <p style="font-size: 16px;"><b>Kod produktu: </b>{kod_produktu}</p>
                <p style="font-size: 12px; margin-right: 10mm">{opis_produktu}</p>
                <p style="font-size: 12px; margin-right: 10mm">Cena: {cena_produktu} PLN netto/szt.</p>
            </span>
        </div>
        """
        containers.insert(counter, element)
        counter += 1

    return containers
