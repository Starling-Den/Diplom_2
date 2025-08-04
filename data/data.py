from data.generators import login_generator, password_generator, name_generator


MAIN_URL = 'https://stellarburgers.nomoreparties.site/'

ENDPOINTS = {
    "ORDER_CREATE": f'{MAIN_URL}api/orders',
    "USER_CREATE": f'{MAIN_URL}api/auth/register',
    "USER_LOGIN": f'{MAIN_URL}api/auth/login',
    "USER_LOGOUT": f'{MAIN_URL}api/auth/logout',
    "USER_TOKEN": f'{MAIN_URL}api/auth/token',
    "USER_DATA": f'{MAIN_URL}api/auth/user',
}

EXISTING_USER = {
    "email": "shpakqa@yandex.ru",
    "password": "Rjktcdj12345",
    "name": "DenisPetrovich",
}

USER_WITHOUT_EMAIL = {
    "email": '',
    "password": f"{password_generator()}",
    "name": f"{name_generator()}",
}

USER_INVALID_DATA = {
    "login": f"{login_generator()}",
    "password": f"{password_generator()}"
}

INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70"]
