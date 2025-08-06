import pytest
import requests

from data.api import *
from data.urls import ENDPOINTS
from data.generators import generate_user_data


@pytest.fixture
def user_create_uniq():
    user_data = generate_user_data()
    requests.post(ENDPOINTS["USER_CREATE"], json=user_data)
    user_login_and_password = {
        "email": user_data["email"],
        "password": user_data["password"],
    }
    yield user_login_and_password
    user_delete(user_data["email"], user_data["password"])

@pytest.fixture
def user_login():
    def login(user_data):
        response = requests.post(ENDPOINTS["USER_LOGIN"], json=user_data)
        return response
    return login
