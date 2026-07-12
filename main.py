from warehouse import show_products, show_menu
from data import products



def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()
        if choice == '1':
            show_products(items=products)
        else:
            print('Нет такой опции')
            break    


if __name__ == "__main__":
    main()