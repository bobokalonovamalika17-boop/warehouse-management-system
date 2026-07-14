# warehouse.py
# Функции которые потом вызываются в файле main.py

import pandas as pd
from data import products


def show_menu():
    """
    Функция выводит главное меню для выбора пользователя.
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
    Функция выводит товары на складе в виде таблицы.
    """
    if not items:
        print("Склад пуст")
    else:
        df = pd.DataFrame(items)
        print(df)


def add_product():
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
    print("Товар добавлен")


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
    