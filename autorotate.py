from time import sleep
from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection


def rotate():
    with Connection('http://admin:2EGDRHHD4TJ@192.168.8.1/') as connection:
        client = Client(connection)
        client.dial_up.set_mobile_dataswitch(0)
        client.dial_up.set_mobile_dataswitch(1)

while(True):
    try:
        rotate()
        sleep(60)
    except:
        pass