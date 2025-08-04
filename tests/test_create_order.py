import pytest
import allure

from data.api import order_create
from data.data import *


class TestCreateOrder:
    @allure.title("Тест создания заказа с авторизацией")
    def test_create_order_auth(self, user_login):
        with allure.step("Отправляем запрос на вход пользователя"):
            response = user_login(EXISTING_USER)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 200
        with allure.step("Получаем токен"):
            auth_token = response.json().get("accessToken")
            token = auth_token.split('Bearer ')[-1] if 'Bearer ' in auth_token else auth_token
            assert token
        with allure.step("Готовим данные и отправляем запрос на создание заказа"):
            order_data = {"ingredients": INGREDIENTS[:3]}
            response = order_create(order_data, token)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 200
            response_json = response.json()
            assert response_json.get("success") is True

    @allure.title("Тест создания заказа без авторизациии")
    def test_create_order_without_auth(self):
        with allure.step("Готовим данные"):
            order_data = {"ingredients": INGREDIENTS[:2]}
        with allure.step("Отправляем запрос на создание заказа"):
            response = order_create(order_data)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 200

    @allure.title("Тест создания заказа с ингредиентами")
    def test_create_order_with_ingredients(self):
        with allure.step("Готовим данные"):
            order_data = {"ingredients": INGREDIENTS[:2]}
        with allure.step("Отправляем запрос на создание заказа"):
            response = order_create(order_data)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 200
            assert response.json().get("success") is True

    @allure.title("Тест создания заказа без ингредиентов")
    def test_create_order_without_ingr(self):
        order_data = {}
        with allure.step("Отправляем запрос на создание заказа"):
            response = order_create(order_data)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 400
            assert response.json().get("success") is False

    @allure.title("тест создания заказа с невалидным хэшем ингредиентов")
    def test_create_order_invalid_hash(self):
        order_data = {"ingredients": ["sdaf23r23r"]}
        response = order_create(order_data)
        assert response.status_code == 500
