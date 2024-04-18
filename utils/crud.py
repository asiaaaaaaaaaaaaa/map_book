def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twój znajomy {user['name']} opublikował: {user['posts']}")

def add_new_user(users:list): -> None:
    new_name: str = input("Enter your name: ")
    new_surname: str = input("Enter your surname: ")
    new_post: int = int(input("Enter your post: "))
    new_username: dict = {"name": new_name, "surname": new_surname, "post": new_post}
    print(new_user)
    users.append(new_user)


def search_users(users) -> None:


kogo_szukasz = input("Kogo szukasz")
for user in users:
    if user in users:
        if user['name'] == kogo_szukasz:
            print(user)

