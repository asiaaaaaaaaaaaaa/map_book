from models.data import users
from utils.crud import show_users


def remove_user(users)-> None:
    Kogo_szukasz=input("Kogo szukasz: ")
    for user in users:
        if user['name']==Kogo_szukasz:
            users.remove(user)

search_user(users)
print(users)