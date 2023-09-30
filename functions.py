import requests
import data
import configuration


# создаем новый заказ.
def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


# получаем номер трека
def get_new_track():
    response = new_order(data.order)
    response_data = response.json()
    return response_data["track"]


# получаем заказ по его номеру
def get_order():
    track_number = "?t=" + str(get_new_track())
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + track_number)

# получаем заказ по его номеру
def get_order():
    track_number = "?t=" + str(get_new_track())
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + track_number)
response_1 = get_order()
print(response_1.json())
print(response_1.status_code)