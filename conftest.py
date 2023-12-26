import pytest
from helpers import *
from data import APILinks


@pytest.fixture(scope='function')
def create_and_delete_courier():
    response, login_pass = register_new_courier_and_return_login_password()
    yield response, login_pass

    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    courier_signin = requests.post(APILinks.main_url + APILinks.login_url, data=payload)
    courier_id = courier_signin.json()["id"]
    requests.delete(APILinks.main_url + APILinks.login_url + str(courier_id))
