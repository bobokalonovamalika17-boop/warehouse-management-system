# data.py
# Начальные данные склада.
# Каждый товар — это словарь с полями: id, name, category, price, quantity.
# По ТЗ при запуске программы в памяти должно быть минимум 10 товаров.

products = [
    {"id": 1,  "name": "Клавиатура", "category": "Электроника", "price": 250.0,  "quantity": 15},
    {"id": 2,  "name": "Мышка",    "category": "Электроника", "price": 120.0,  "quantity": 40},
    {"id": 3,  "name": "Ноутбук",   "category": "Электроника", "price": 1500.0, "quantity": 8},
    {"id": 4,  "name": "Монитор",  "category": "Электроника", "price": 800.0,  "quantity": 12},
    {"id": 5,  "name": "Яблоко",    "category": "Еда",        "price": 5.0,    "quantity": 200},
    {"id": 6,  "name": "Хлеб",    "category": "Еда",        "price": 3.5,    "quantity": 150},
    {"id": 7,  "name": "Вода",    "category": "Еда",        "price": 2.0,    "quantity": 300},
    {"id": 8,  "name": "Стул",    "category": "Мебель",   "price": 90.0,   "quantity": 35},
    {"id": 9,  "name": "Стол",    "category": "Мебель",   "price": 220.0,  "quantity": 20},
    {"id": 10, "name": "Телефон",    "category": "Электроника", "price": 950.0,  "quantity": 25},
]