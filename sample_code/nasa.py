import requests


def nasa_image():
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': 'DEMO_KEY'}
    response = requests.get(url, params).json()
    image = response['hdurl']
    return image
