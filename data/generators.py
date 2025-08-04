from faker import Faker


fake = Faker()

def login_generator():
    login_gen = fake.user_name()
    return f'{login_gen}'

def password_generator():
    password_gen = fake.random_number(7)
    return f'{password_gen}'

def name_generator():
    name_gen = fake.first_name()
    return f'{name_gen}'

def generate_user_data():
    email = login_generator()
    password = password_generator()
    name = name_generator()
    return {
        "email": f"{email}@ya.ru",
        "password": f"{password}",
        "name": f"{name}",
    }
