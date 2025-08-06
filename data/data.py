from data.generators import login_generator, password_generator, name_generator


EXISTING_USER = {
    "email": "shpakqa@yandex.ru",
    "password": "Rjktcdj12345",
    "name": "DenisPetrovich",
}
USER_DATA_WITHOUT_FIELDS= [
    {"email": '', "password": f"{password_generator()}", "name": f"{name_generator()}",},
    {"email": f"{login_generator()}","password": '', "name": f"{name_generator()}",},
    {"email": f"{login_generator()}","password": f"{password_generator()}","name": '',}
]

USER_INVALID_DATA = {
    "login": f"{login_generator()}",
    "password": f"{password_generator()}"
}

INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70"]
