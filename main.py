# main.py
# Главное меню
# Отображается главное меню где пользователь может выбрать категории

from warehouse import show_menu, show_products, add_product, delete_product

from data import products


def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_products(items=products)
        elif choice == '2':
            add_product()
        elif choice == '3':
            delete_product()   
        else:
            print("Нет такой опции")
            break


if __name__ == "__main__":
    main()
