import requests
import pandas as pd
from bs4 import BeautifulSoup as BS


# Функция для определения последней страницы в категории
def get_last_page(url):
    response = requests.get(url, verify=False)
    soup = BS(response.text, 'lxml')

    # Находим блок с пагинацией
    pagination = soup.find('div', class_='bx-pagination-container')

    if pagination:
        # Ищем все ссылки пагинации внутри этого блока
        page_numbers = [int(a.get_text(strip=True)) for a in pagination.find_all('a') if
                        a.get_text(strip=True).isdigit()]
        if page_numbers:
            return max(page_numbers)  # Возвращаем максимальное число - последняя страница
    return 1  # Если пагинации нет, то возвращаем 1 (одна страница)


# Парсинг товаров со всех категорий и страниц
def parser(url: str):
    data = []

    # Запрашиваем главную страницу, чтобы найти все категории
    response = requests.get(url, verify=False)
    soup = BS(response.text, 'lxml')
    catalog_list = soup.find('ul', class_='catalog').find_all('a')

    # Проходим по каждой категории
    for category in catalog_list:
        category_name = category.get_text(strip=True)
        category_href = category.get('href').replace('/zp', '')
        category_url = f'{url}{category_href}'

        # Определяем количество страниц в текущей категории
        last_page = get_last_page(category_url)
        print(f"Категория: {category_name}, URL: {category_url}, Последняя страница: {last_page}")

        # Проходим по каждой странице категории
        for page_number in range(1, last_page + 1):
            page_url = f'{category_url}?PAGEN_1={page_number}'
            print(f"Парсинг страницы: {page_url}")

            res = requests.get(page_url)
            soup_page = BS(res.text, 'lxml')

            # Находим все товары на странице
            items = soup_page.find_all('div', class_='card')
            if not items:
                print(f"На странице {page_url} товары не найдены.")

            for item in items:
                # Находим наименование товара
                item_name = item.find('div', class_='name').find('a').get_text(strip=True)

                # Находим артикул товара и проверяем его наличие
                artikul_div = item.find('div', class_='artikul')
                item_artikul = 'Нет артикула'
                if artikul_div:
                    item_artikul = artikul_div.get_text(strip=True).replace('артикул', '').strip()

                # Находим цену товара и обрабатываем цены с исключением
                try:
                    item_price = item.find('div', class_='price').find_all('span')[1].get_text(strip=True)
                except (IndexError, AttributeError):
                    item_price = 'Нет цены'

                print(f"Товар: {item_name}, Артикул: {item_artikul}, Цена: {item_price}")

                # Добавляем данные в список
                data.append({
                    'Категория': category_name,
                    'Наименование': item_name,
                    'Артикул': item_artikul,
                    'Цена': item_price
                })
    df = pd.DataFrame(data)
    df.to_excel('products.xlsx', index=False)


# URL главной страницы
url = 'https://www.kamazik.ru/zp'
parser(url)