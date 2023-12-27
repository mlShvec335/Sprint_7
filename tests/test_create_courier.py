import pytest
import allure
from helpers import *
from conftest import create_and_delete_courier, create_and_delete_unregistered_courier
from data import CourierData, APILinks


class TestCreateCourier:
    @allure.title('Успешное создание нового курьера')
    def test_create_courier(self, create_and_delete_unregistered_courier):
        payload = create_and_delete_unregistered_courier
        r = requests.post(APILinks.MAIN_URL + APILinks.COURIER_URL, data=payload)
        assert r.status_code == 201 and r.text == '{"ok":true}'

    @allure.title('Нельзя создать одинаковых курьеров')
    def test_create_the_same_courier(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier[1][0],
            "password": create_and_delete_courier[1][1],
            "firstName": create_and_delete_courier[1][2]
        }
        r = requests.post(APILinks.MAIN_URL + APILinks.COURIER_URL, data=payload)
        assert r.status_code == 409 and r.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Курьер не создается без обязательных данных')
    @pytest.mark.parametrize('courier_data', (
            CourierData.without_login,
            CourierData.without_password,
            CourierData.empty_login_courier,
            CourierData.empty_password_courier))
    def test_create_courier_no_data(self, courier_data):
        r = requests.post(APILinks.MAIN_URL + APILinks.COURIER_URL, data=courier_data)
        assert r.status_code == 400 and r.json()['message'] == "Недостаточно данных для создания учетной записи"
