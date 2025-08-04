import pytest
import allure

from data.api import *
from data.data import *


class TestUserCreate:
    @allure.title('Тест создания уникального пользователя')
    def test_user_create_uniq(self, user_create_uniq):
        user_data = user_create_uniq
        response = user_login(user_data)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 200

    @allure.title("Тест создания уже зарегистрированного пользователя")
    def test_exist_user_create(self):
        with allure.step("Отправляем запрос на повторное создание пользователя"):
            response = user_register(EXISTING_USER)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 403
            response_json = response.json()
            assert response_json.get("message") == "User already exists"
            assert response_json.get("success") is False

    @allure.title("Тест создания пользователя без заполнения обязательных полей")
    def test_user_create_without_fields(self):
        with allure.step("Отправляем запрос без емейла"):
            response = user_register(USER_WITHOUT_EMAIL)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 403
            response_json = response.json()
            assert response_json.get("success") is False
            assert response_json.get("message") == "Email, password and name are required fields"
