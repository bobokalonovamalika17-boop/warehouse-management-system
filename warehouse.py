# warehouse.py
# Функции которые потом вызываются в файле main.py

import pandas as pd
from data import products
import datetime

def show_menu():
    """
    Функция выводит главное меню с выбором опций где пользователь может выбрать по номеру.
    """
    print()
    print("===========================")
    print("WAREHOUSE MANAGEMENT SYSTEM ")
    print("===========================")
    print()
    print("1. Показать товары")
    print("2. Добавить товар")
    print("3. Удалить товар")
    print("4. Изменить товар")
    print("5. Найти товар")
    print("6. Продать товар")
    print("7. Пополнить склад")
    print("8. Показать категории")
    print("9. Статистика ")
    print("0. Выход")
    print()


def show_products(items: list):
    """
    Функция выводит товары на складе в виде таблицы. Если товаров нет на складе выводит "Склад пуст".
    """
    if not items:
        print("Склад пуст")
    else:
        df = pd.DataFrame(items)
        print(df)


def add_product():
    """
    Функция добавляет
    """
    if products == []:
        new_id = 1
    else:
        new_id = products[-1]["id"] + 1
    name = input("Название: ")
    category = input("Категория: ")
    price = input("Цена: ")
    quantity = input("Количество: ")
    thisdict = {
        "id": new_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
    }
    products.append(thisdict)
    print("Товар добавлен.")


def delete_product():
    id_to_delete = int(input("Введите ID товара: "))

    for product in products:
        if product["id"] == id_to_delete:
            products.remove(product)
            print("Товар удален.")
            break
    else:
        print("Товар не найден.")


def update_product():
    id_to_update = int(input("Введите ID товара: "))
    
    for product in products:
        if product['id'] == id_to_update:
            product['name'] = input("Название: ")
            product['category'] = input("Категория: ")
            product['price'] = input("Цена: ")
            product['quantity'] = input("Количество: ")
            print("Данные успешно обновлены.")
            break
    else:
        print("Нет такого товара.")  


def search_products():
    name_to_search = (input('Введите название товара: ')).lower()

    for product in products:
        if name_to_search in product['name'].lower():
            print(product['name'])
            break
    else:
            print('Нет такого товара.')    


def sell_products():
    id_to_sell = int(input('Введите ID товара: '))
    quantity_to_sell = int(input('Введите количество товара: '))
    x = datetime.datetime.now()

    for product in products:
            if id_to_sell == product['id'] and quantity_to_sell <= product['quantity']:
                product["quantity"] -= quantity_to_sell
                print('Продано успешно.')
                print(f"Дата продажи: {x}")
                print(f'Количество: {quantity_to_sell}')
                print(f"Остаток: {product['quantity']}")
                break
    else:
        print('Недостаточно товара.')


def restock_product():
    id_to_restock = int(input('Введите ID товара: '))
    quantity_to_restock = int(input('Введите количество товара: '))

    for product in products:
        if id_to_restock == product['id']:
            product['quantity'] += quantity_to_restock
            print('Остаток успешно пополнен.')
            break
    else:
        print("Нет такого товара.")


def show_categories():
    categories = set()

    for product in products:
        categories.add(product["category"])
    for category in categories:
            print(category)
    

def show_statistics():
    quantity_of_items = 0
    categories = set()
    price_of_products = 0

    for product in products:
        quantity_of_items += product['quantity']
        categories.add(product["category"])
        price_of_products += product['price']
    
        
    print(f"Всего товаров: {len(products)}")
    print(f"Категорий: {len(categories)}")
    print(f'Всего единиц товара: {quantity_of_items}')
    print(f'Стоимость склада: {price_of_products}')
    print(f'Самый дорогой товар: {max(product["price"] for product in products)}')
    print(f'Самый дешевый товар: {min(product["price"] for product in products)}')
    print(f'Средняя цена товара: {price_of_products / quantity_of_items}')
    print(f'Среднее количество товара: {quantity_of_items / len(products)}')
    


















