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


def get_country_by_language(language: str) -> dict:
    response = requests.get(f'{COUNTRY_BASE_URL}lang/{language}')

    if response.status_code != 200:
        raise ValueError('Country not found.')

    return response.json()[0]


def get_country_data(country: dict) -> str:
    data = ''
    data += f"Name (official): {country['name']['official']}\n"
    data += f"Name (common): {country['name']['common']}\n"
    data += f"Capital(s): {' ,'.join(country['capital'])}\n"
    data += f"Languages: {', '.join(country['languages'].values())}\n"
    data += f"Region: {country['region']}\n"
    data += f"Subregion: {country['subregion']}\n"
    data += f"Area: {country['area']} km²\n"
    data += f"Currency: {', '.join(country['currencies'].keys())}\n"
    data += f"TLD (Top Level Domain): {', '.join(country['tld'])}\n"
    data += f"Demonyms (Male): {country['demonyms']['eng']['m']}\n"
    data += f"Demonyms (Female): {country['demonyms']['eng']['f']}\n"
    data += f"Is independent?: {country['independent']}\n"
    data += f"Is United Nations member?: {country['unMember']}\n"
    data += f"Start Of the Week: {country['startOfWeek'].capitalize()}\n"
    data += f"Postal Code format: {country['postalCode']['format']}\n"

    return data


def get_regions() -> list:
    response = requests.get(f'{COUNTRY_BASE_URL}all?fields=region')

    if response.status_code != 200:
        raise ValueError('Country not found.')

    return list(sorted({country['region'] for country in response.json()}))


def get_subregions(region: str) -> list:
    response = requests.get(f'{COUNTRY_BASE_URL}region/{region}?fields=subregion')

    if response.status_code != 200:
        raise ValueError('Country not found.')

    return list(sorted({country['subregion'] for country in response.json()}))


def get_countries_by_subregion(subregion: str) -> list:
    response = requests.get(f'{COUNTRY_BASE_URL}subregion/{subregion}?fields=name')

    if response.status_code != 200:
        raise ValueError('Country not found.')

    return list(sorted({country['name']['common'] for country in response.json()}))


def get_country_borders_names(country: dict) -> list:
    response = requests.get(f'{COUNTRY_BASE_URL}alpha?codes={",".join(country["borders"])}&fields=name')

    if response.status_code != 200:
        raise ValueError('Country not found.')

    return list(sorted({country['name']['common'] for country in response.json()}))
