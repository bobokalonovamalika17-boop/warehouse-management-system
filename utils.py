# utils.py
# Вспомогательные функции для валидации ввода пользователя

def input_menu()-> int:
    '''
    Функция запрашивает ввод действия пользователя, проверяет, что введены только цифры, что число от 1 до 9 и возвращаает число как int. 
    '''
    while True:
        choice = input("Выберите действие: ").strip()

        
        if not choice.isdigit():
            print("Введите корректное число.")
            continue
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Нет такой опции.")
            continue

        return int(choice)
    
    
def input_name()-> str:
    '''
    Функция запрашивает ввод названия товара, проверяет чтобы название не было пустым, возвращает строку.
    '''
    while True:
            name = input("Введите название товара: ")

            if name == "":
                print("Название не может быть пустым.")
                continue

            return name  


def input_category()-> str:
    '''
    Функция запрашивает ввод категории товара, проверяет чтобы категория не было пустым, возвращает строку.
    '''
    while True:
            category = input("Введите категорию товара: ")

            if category == "":
                print("Категория не может быть пустым.")
                continue
            
            return category




def input_price()-> float:
    '''
    Функция запрашивает ввод цены товара, превращает число в float, проверяет число на отрицательность, возвращает число.
    '''
    while True:
        price = input("Введите цену товара: ")
        price = float(price)

        if price < 0:
            print('Цена не может быть отрицательной.')
            continue


        return price



def input_quantity()-> int:
    '''
    Функция запрашивает ввод количества товара, проверяет, что введены только цифры, пребразовывает число в int,проверяет число на отрицательность, возвращает число.
    '''
    while True:
            quantity = input("Введите количество товара: ")
            
            if not quantity.isdigit():
                print("Введите корректное число.")
                continue

            quantity = int(quantity)

            if quantity < 0:
                print('Количество не может быть отрицательным.')
                continue


            return quantity

def input_id()-> int:
    '''
    Функция запрашивает ввод ID товара, проверяет, что введены только цифры, возвращает число как int.
    '''
    while True:
        id_to_input = input("Введите ID товара: ")
        
        if not id_to_input.isdigit():
            print("Введите корректное число.")
            continue

        return int(id_to_input)


          
def input_name_to_search()-> str:
    '''
    Функция запрашивает у пользователя название товара для поиска,
    проверяет, что ввод не пустой, и возвращает введенную строку
    для поиска товара по названию.
    '''
    while True:
            name = (input('Введите название товара: ')).lower()

            if name == "":
                print("Название не может быть пустым.")
                continue

            return name  