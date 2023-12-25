import pytest
import allure
from helpers import *
from conftest import delete_courier
from data import APILinks, CourierData


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    def test_login_courier(self, delete_courier):
        payload = {"login": delete_courier[1][0],
                   "password": delete_courier[1][1]}
        r = requests.post(APILinks.main_url + APILinks.login_url, data=payload)
        assert r.status_code == 200 and 'id' in r.json()

    @allure.title('Вход невозможен без логина или пароля')
    @pytest.mark.parametrize('courier_data', (
            CourierData.empty_login,
            CourierData.empty_password,
            CourierData.only_password,
            CourierData.only_login))
    def test_login_courier_without_data(self, courier_data):
        payload = courier_data
        r = requests.post(APILinks.main_url + APILinks.login_url, data=payload)
        assert r.status_code == 400 and r.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Вход невозможен c несуществующей парой логин-пароль')
    def test_login_courier_with_fail_data(self, delete_courier):
        payload = {"login": delete_courier[1][1],
                   "password": delete_courier[1][0]}
        r = requests.post(APILinks.main_url + APILinks.login_url, data=payload)
        assert r.status_code == 404 and r.json()['message'] == 'Учетная запись не найдена'
