from models.data import users
from utils.crud import show_users


def update_user(users)-> None:
    Kogo_szukasz=input("Kogo szukasz: ")
    for user in users:
        if user['name']==Kogo_szukasz:
            user['name']=input("podaj nowe imie:")
            user['surname']=input("podaj nowe nazwisko:")
            user['posts']=input("podaj nowe liczba postów:")
print(users)
update_user(users)
print(users)