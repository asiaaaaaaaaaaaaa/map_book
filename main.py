from models.data import users
from utils.crud import show_users
1

if __name__ == '__main__':
    print("Witaj użutkowniku")
    while True:

        print("Wybierz opcję menu")
        print("1. Wyświetl co u znajomych")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)
