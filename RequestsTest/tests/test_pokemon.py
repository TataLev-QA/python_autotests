import requests
import pytest

url = 'https://api.pokemonbattle.me/v2'
token = 'af2c141c55a6d7458103edd5c7030953'
header = {'Content-Type' : 'application/json', 'trainer_token': token}
trainer_id = '2569'


def test_status_code():
    response = requests.get(url = f'{url}/trainers',params = {'sort': 'desc_price'})
    assert response.status_code == 200


def test_part_of_response_name():
    response_name = requests.get(url = f'{url}/trainers', params = {'trainer_id': trainer_id }) 
    assert response_name.json()["data"][0]["trainer_name"] == "Tata Lev"
