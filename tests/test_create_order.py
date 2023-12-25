import pytest
import allure
import json
from helpers import *
from data import APILinks, OrderData


class TestCreateOrder:
    @allure.title('Создание заказа с разными цветами')
    @pytest.mark.parametrize('color', (["BLACK"], ["GREY"], ["BLACK", "GREY"], []))
    def test_create_order(self, color):
        OrderData.order_data["color"] = [color]
        payload = json.dumps(OrderData.order_data)
        r = requests.post(APILinks.main_url + APILinks.main_orders_url, data=payload)
        assert r.status_code == 201 and 'track' in r.text
