from models.data import users
from utils.crud import show_users

print(users)
new_name: str = input("Enter your name: ")
new_surname: str = input("Enter your surname: ")
new_post: int = int(input("Enter your post: "))
new_username: dict = {"name": new_name, "surname": new_surname, "post": new_post}
print(new_user)
users.append(new_user)
print(users)


def add_new_user(users:list)->None:
    new_name: str = input("Enter your name: ")
     new_surname: str = input("Enter your surname: ")
    new_post: int = int(input("Enter your post: "))
    new_username: dict = {"name": new_name, "surname": new_surname, "post": new_post}
    print(new_user)
    users.append(new_user)





def search_users(users)->None:

kogo szukasz=input("Kogo szukasz")
for user in users:
      if user in users:
         if user['name']==kogo_szukasz:
            users.remove(user)
              print(users)

search_user(users)

