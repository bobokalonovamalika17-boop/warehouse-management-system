# warehouse.py
# Функции которые потом вызываются в файле main.py

import pandas as pd
from data import products
import datetime
from utils import input_price, input_name, input_category, input_quantity, input_id, input_name_to_search


def show_menu()-> str:
    """
    Функция выводит главное меню с выбором опций где пользователь может выбрать по номеру определенные действия. После выполнения любого действия программа снова возвращается в меню. 

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


def show_products(items: list)-> None:
    """
    Функция выводит товары на складе в виде таблицы. Если товаров нет на складе выводит "Склад пуст".
    """
    if not items:
        print("Склад пуст")
    else:
        df = pd.DataFrame(items)
        print(df)


def add_product()-> None:
    """
    Функция добавляет товар в склад, запрашивая ввод названия, категории, цены и количества товара, создает словарь, назначает новый ID, добавляет словарь в список товаров и выводит "Товар успешно добавлен".
    """
    if products == []:
        new_id = 1
    else:
        new_id = products[-1]["id"] + 1
    name = input_name()
    category = input_category()
    price = input_price()
    quantity = input_quantity()
    thisdict = {
        "id": new_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
    }
    products.append(thisdict)
    print("Товар добавлен.")


def delete_product()-> None:
    '''
    Функция удаляет товар, запрашивая у пользователя ID товара. Если товар найден выводит "Товар удален", если не найден "Товар не найден".
    '''
    id_to_delete = input_id()

    for product in products:
        if product["id"] == id_to_delete:
            products.remove(product)
            print("Товар удален.")
            break
    else:
        print("Товар не найден.")


def update_product()-> None:
    """
    Функция изменяет товар, запрашивая у пользователя ID существующего товара. Если товар найден выводит "Данные успешно обновлены", если не найден выводит "Нет такого товара".
    """
    id_to_update = input_id()

    for product in products:
        if product['id'] == id_to_update:
            product['name'] = input_name()
            product['category'] = input_category()
            product['price'] = input_price()
            product['quantity'] = input_quantity()
            print("Данные успешно обновлены.")
            break
    else:
        print("Нет такого товара.")  


def search_products()-> str:
    """
    Функция делает поиск товара по названию и выводит найденный товар.
    """
    name_to_search = input_name_to_search()

    for product in products:
        if name_to_search in product['name'].lower():
            print(product['name'])
            break
    else:
            print('Нет такого товара.')    


def sell_products()-> None:
    """
    Функция продает товар, запрашивая у пользователя ввод ID товара и количество товара, проверяет существует ли товар, хватает ли количества, если хватает уменьшает количество и выводит "Продано успешно", дату продажи, количество и остаток. Если количество недостаточно выводит "Недостаточно товара".
    """
    id_to_sell = input_id()
    quantity_to_sell = input_quantity()
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


def restock_product()-> None:
    """
    Функция пополняет склад, запращивая у пользователя ID нового товара и его количество, выводит "Остаток успешно пополнен".
    """
    id_to_restock = int(input('Введите ID товара: '))
    quantity_to_restock = int(input('Введите количество товара: '))

    for product in products:
        if id_to_restock == product['id']:
            product['quantity'] += quantity_to_restock
            print('Остаток успешно пополнен.')
            break
    else:
        print("Нет такого товара.")


def show_categories()-> None:
    """
    Функция выводит все уникальные категории.
    """
    categories = set()

    for product in products:
        categories.add(product["category"])
    for category in categories:
            print(category)
    

def show_statistics()-> str:
    """
    Функция показывает статистику, а именно:
    - количество товаров, 
    - количество категорий,
    - общее количество единиц товара,
    - общую стоимость склада,
    - самый дорогой товар,
    - самый дешевый товар,
    - среднюю цену товара,
    - среднее количество товара.
    """
    quantity_of_items = 0 
    categories = set()
    price_of_products = 0

    for product in products:
        quantity_of_items += product['quantity']
        categories.add(product["category"])
        price_of_products += product['price']

    most_expensive = products[0]
    least_expensive = products[0]

    for product in products:
        if product['price'] < least_expensive['price']:
            least_expensive = product
        elif product["price"] > most_expensive["price"]:
            most_expensive = product
    
        
    print(f"Всего товаров: {len(products)}")
    print(f"Категорий: {len(categories)}")
    print(f'Всего единиц товара: {quantity_of_items}')
    print(f'Стоимость склада: {price_of_products}')
    print(f'Самый дорогой товар: {most_expensive["name"]}')
    print(f'Самый дешевый товар: {least_expensive["name"]}')
    print(f'Средняя цена товара: {price_of_products / len(products)}')
    print(f'Среднее количество товара: {quantity_of_items / len(products)}')
    


















