import allure
from helpers import *
from data import APILinks


class TestGetOrdersList:
    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        r = requests.get(APILinks.MAIN_URL + APILinks.ORDERS_URL)
        orders_list = r.json()["orders"]
        assert r.status_code == 200 and type(orders_list) == list
