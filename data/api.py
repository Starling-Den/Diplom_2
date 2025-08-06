import pytest
import allure
import requests

from data.urls import ENDPOINTS


@allure.step("Создание заказа")
def order_create(order_data, token=None):
    headers = {}
    if token:
        headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(ENDPOINTS["ORDER_CREATE"], json=order_data, headers=headers)
    return response

@allure.step("Создание пользователя")
def user_register(user_data):
    response = requests.post(ENDPOINTS["USER_CREATE"], json=user_data)
    return response

@allure.step("Получение accessToken")
def get_access_token(email, password):
    response = requests.post(ENDPOINTS["USER_LOGIN"], json={"email": email, "password": password,})
    return response.json().get("accessToken")

@allure.step("Удалить пользователя")
def user_delete(email, password):
    access_token = get_access_token(email, password)
    requests.delete(ENDPOINTS["USER_DATA"], headers={"Authorization": f"Bearer {access_token}"})

@allure.step("Логин пользователя")
def user_login(user_data):
    response = requests.post(ENDPOINTS["USER_LOGIN"], json=user_data)
    return response
