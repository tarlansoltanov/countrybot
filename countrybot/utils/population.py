import matplotlib.pyplot as plt
import requests
import logging

BASE_URL = 'https://population.un.org/dataportalapi/api/v1/'

def get_location_id(code: str) -> int:
    response = requests.get(f'{BASE_URL}locations/{code}?sort=id&format=json')

    if response.status_code != 200:
        raise ValueError('Location not found.')
    
    return response.json()[0]['id']


def total_population_graph(code: str) -> str:
    location_id = get_location_id(code)
    indicator_id = 49

    response = requests.get(f'{BASE_URL}data/indicators/{indicator_id}/locations/{location_id}?startYear=2000&pagingInHeader=false&format=json')

    if response.status_code != 200:
        raise ValueError('Data not found.')
    
    data = list(filter(lambda x: x['sexId'] == 3, response.json()['data']))

    x  = [int(item['timeLabel']) for item in data]
    y = [int(item['value']) for item in data]

    print(len(x), x)
    print(len(y), y)

    plt.plot(x, y, color='green')
    plt.xlabel('Year')
    plt.ylabel('Population')

    plt.savefig('media/population.png')
    plt.clf()

    return 'media/population.png'


def men_population_graph(code: str) -> str:
    location_id = get_location_id(code)
    indicator_id = 49

    response = requests.get(f'{BASE_URL}data/indicators/{indicator_id}/locations/{location_id}?startYear=2000&pagingInHeader=false&format=json')

    if response.status_code != 200:
        raise ValueError('Data not found.')
    
    data = list(filter(lambda x: x['sexId'] == 1, response.json()['data']))

    x  = [int(item['timeLabel']) for item in data]
    y = [int(item['value']) for item in data]

    print(len(x), x)
    print(len(y), y)

    plt.plot(x, y, color='green')
    plt.xlabel('Year')
    plt.ylabel('Population')

    plt.savefig('media/population.png')
    plt.clf()

    return 'media/population.png'


def women_population_graph(code: str) -> str:
    location_id = get_location_id(code)
    indicator_id = 49

    response = requests.get(f'{BASE_URL}data/indicators/{indicator_id}/locations/{location_id}?startYear=2000&pagingInHeader=false&format=json')

    if response.status_code != 200:
        raise ValueError('Data not found.')
    
    data = list(filter(lambda x: x['sexId'] == 2, response.json()['data']))

    x  = [int(item['timeLabel']) for item in data]
    y = [int(item['value']) for item in data]

    print(len(x), x)
    print(len(y), y)

    plt.plot(x, y, color='green')
    plt.xlabel('Year')
    plt.ylabel('Population')

    plt.savefig('media/population.png')
    plt.clf()

    return 'media/population.png'