class APILinks:
    main_url = 'https://qa-scooter.praktikum-services.ru/'
    login_url = 'api/v1/courier/login'
    courier_url = 'api/v1/courier/'
    main_orders_url = 'api/v1/orders'


class CourierData:
    only_login = {"login": "test"}
    only_password = {"password": "test"}
    empty_password = {"login": "test", "password": ""}
    empty_login = {"login": "", "password": "test"}
    without_login = {"password": "test", "firstName": 'test'}
    without_password = {"login": "test", "firstName": "test"}
    empty_login_courier = {"login": "", "password": "test", "firstName": "test"}
    empty_password_courier = {"login": "test", "password": "", "firstName": "test"}


class OrderData:
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. тестовая, д.1",
        "metroStation": 4,
        "phone": "+7 999 123 45 67",
        "rentTime": 5,
        "deliveryDate": "2023-12-23",
        "comment": "оставить у двери"
    }
