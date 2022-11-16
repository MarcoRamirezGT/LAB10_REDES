from kafka import KafkaProducer
import random
import matplotlib.pyplot as plt
import json
import sys


def generate_random_number_gaussian():
    return int(random.gauss(50, 20))


def generate_random_float_number_gaussian():
    return random.gauss(50, 20)


def get_random_cardinal_point():
    cardinal_points = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return cardinal_points[random.randint(0, 7)]


def get_random_values():
    return {"temperature": generate_random_float_number_gaussian(), "humidity": generate_random_number_gaussian(), "wind_direction": get_random_cardinal_point()}


# from json to bytes

def json_to_bytes(x):
    return json.dumps(x).encode('utf-8')


x = json_to_bytes(get_random_values())

# get size of x in bytes


def get_size(x):
    return sys.getsizeof(x)


print(get_size(x))

# producer = KafkaProducer(bootstrap_servers='lab10.alumchat.fun')

# for i in range(10):
#     x = get_random_values()
#     print('Mensaje enviado: ', x)
#     producer.send('19588', json.dumps(x).encode('utf-8'))
#     plt.pause(5)
