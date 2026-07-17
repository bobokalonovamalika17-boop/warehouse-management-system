# main.py
# Главное меню
# Отображается главное меню где пользователь может выбрать категории

from warehouse import show_menu, show_products, add_product, delete_product, update_product, search_products, sell_products, restock_product, show_categories,  show_statistics
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
        elif choice == '4':
            update_product()
        elif choice == '5':
            search_products() 
        elif choice == '6':
            sell_products()
        elif choice == '7':
            restock_product()
        elif choice == '8':
            show_categories()
        elif choice == '9':
            show_statistics()
        else:
            print("Нет такой опции.")
            break


if __name__ == "__main__":
    main()
