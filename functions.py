import requests
import data
import configuration


# создаем новый заказ.
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=body)


# получаем номер трека и подготавливаем его к формату запроса
def get_new_track():
    response = post_new_order(data.order)
    response_data = response.json()
    track_number = "?t=" + str(response_data["track"])
    return track_number


# получаем заказ по его номеру
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + track_number)
