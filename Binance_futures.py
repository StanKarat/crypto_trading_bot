import logging
import requests


def get_contracts():

    responce_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    print(responce_object.status_code)

    list_contracts = []

    for contract in responce_object.json()['symbols']:
        list_contracts.append(contract['pair'])

    return list_contracts



print(get_contracts())
