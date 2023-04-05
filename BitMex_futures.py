import requests




def get_contracts():

    responce_object = requests.get("https://www.bitmex.com/api/v1/instrument/active")
    print(responce_object.status_code)

    list_contracts = []

    for contract in responce_object.json():
        list_contracts.append(contract['symbol'])

    return list_contracts



print(get_contracts())
