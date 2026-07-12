# data.py
# Начальные данные склада.
# Каждый товар — это словарь с полями: id, name, category, price, quantity.
# По ТЗ при запуске программы в памяти должно быть минимум 10 товаров.

products = [
    {"id": 1,  "name": "Keyboard", "category": "Electronics", "price": 250.0,  "quantity": 15},
    {"id": 2,  "name": "Mouse",    "category": "Electronics", "price": 120.0,  "quantity": 40},
    {"id": 3,  "name": "Laptop",   "category": "Electronics", "price": 1500.0, "quantity": 8},
    {"id": 4,  "name": "Monitor",  "category": "Electronics", "price": 800.0,  "quantity": 12},
    {"id": 5,  "name": "Apple",    "category": "Food",        "price": 5.0,    "quantity": 200},
    {"id": 6,  "name": "Bread",    "category": "Food",        "price": 3.5,    "quantity": 150},
    {"id": 7,  "name": "Water",    "category": "Food",        "price": 2.0,    "quantity": 300},
    {"id": 8,  "name": "Chair",    "category": "Furniture",   "price": 90.0,   "quantity": 35},
    {"id": 9,  "name": "Table",    "category": "Furniture",   "price": 220.0,  "quantity": 20},
    {"id": 10, "name": "Phone",    "category": "Electronics", "price": 950.0,  "quantity": 25},
]