Sprint_7

Тестирование API учебного сервиса Яндекс Самокат:

I. Создание курьера
1. test_create_courier - курьера можно создать
2. test_create_the_same_courier - нельзя создать двух одинаковых курьеров
3. test_create_courier_no_data - курьер не создается без обязательных данных

II. Логин курьера
1. test_login_courier - курьер может авторизоваться
2. test_login_courier_without_data - вход невозможен без логина или пароля
3. test_login_courier_with_fail_data - вход невозможен c несуществующей парой логин-пароль

III. Создание заказа
1. test_create_order - создание заказа с разными цветами

IV. Список заказов
1. test_get_orders_list - получение списка заказов

- Отчёты о тестировании в allure_results