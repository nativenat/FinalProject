
import configuration
import requests
import data
import sendor_stand_request

# Автотест
def test_order_creation_and_retrieval():
    response = sendor_stand_request.create_order(data.order_body)

    track_number = response.json()["track"]

    # Получение данных заказа по треку
    order_response = sendor_stand_request.get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
