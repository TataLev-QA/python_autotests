import requests

url = 'https://api.pokemonbattle.me/v2'
token = 'af2c141c55a6d7458103edd5c7030953'
id = '1086'
header = {'Content-Type' : 'application/json', 'trainer_token': token}

body_Creation = {
    "name": "Мики",
    "photo": "https://dolnikov.ru/pokemons/albums/777.png"
}

body_change = {
    "pokemon_id": "27755",
    "name": "МикиМики",
    "photo": "https://dolnikov.ru/pokemons/albums/512.png"
}

body_catch = {
    "pokemon_id": "27755"
}


'''response_Creation = requests.post(url = f'{url}/pokemons', headers = header, json = body_Creation)
print(response_Creation.text)

response_change = requests.post(url = f'{url}/pokemons', headers = header, json = body_change)
print(response_change.text)
'''

response_catch = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_catch)
print(response_catch.text)















