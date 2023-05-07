import requests

COUNTRY_BASE_URL = 'https://restcountries.com/v3.1/'


def get_country_by_name(name: str) -> dict:
    response = requests.get(f'{COUNTRY_BASE_URL}name/{name}?fullText=true')

    if response.status_code != 200:
        raise ValueError('Country not found.')

    return response.json()[0]


def get_country_by_code(code: str) -> dict:
    response = requests.get(f'{COUNTRY_BASE_URL}alpha/{code}')

    if response.status_code != 200:
        raise ValueError('Country not found.')

    return response.json()[0]


def get_country_by_capital(capital: str) -> dict:
    response = requests.get(f'{COUNTRY_BASE_URL}capital/{capital}')

    if response.status_code != 200:
        raise ValueError('Country not found.')

    return response.json()[0]


def get_country_data(country: dict) -> str:
    data = ''
    data += f"Name (official): {country['name']['official']}\n"
    data += f"Name (common): {country['name']['common']}\n"
    data += f"Capital(s): {' ,'.join(country['capital'])}\n"
    data += f"Region: {country['region']}\n"
    data += f"Subregion: {country['subregion']}\n"
    data += f"Area: {country['area']} km²\n"
    data += f"Currency: {', '.join(country['currencies'].keys())}\n"
    data += f"Is independent: {country['independent']}\n"

    return data
