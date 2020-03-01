import requests

def json_parser(url):
    data = requests.get(url)
    parsed = data.json()
    print(parsed['data'][0]['Brand'][0]['PCA'][0])
