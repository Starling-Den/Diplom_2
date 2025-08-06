import pytest
import allure

from data.data import EXISTING_USER, USER_INVALID_DATA


class TestUserLogin:
    @allure.title("Тест входа пользователя с валидными данными")
    def test_login_valid_data_true(self, user_login):
        with allure.step("Запрос на вход с ранее зареганным пользователем"):
            response = user_login(EXISTING_USER)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 200
            response_json = response.json()
            assert response_json.get("success") is True
            assert all(key in response_json for key in ["accessToken", "refreshToken", "user"])

    @allure.title("Тест входа пользователя с неверным логином и паролем")
    def test_login_invalid_data(self, user_login):
        with allure.step("Отправялем запрос на вход с невалидными данными"):
            response = user_login(USER_INVALID_DATA)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 401
            response_json = response.json()
            assert response_json.get("success") is False
            assert response_json.get("message") == "email or password are incorrect"
