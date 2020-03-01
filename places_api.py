import json
import requests

api_key = 'AIzaSyBzjLAINirGIEr8AaYYzhU7G8bxTgeDbGs'

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


def finder(query):
    r = requests.get(url + 'query=' + query + '&key=' + api_key)
    x = r.json()
    y = x['results']
    s = []
    for i in range(len(y)):
        lat = y[i]['geometry']['location']['lat']
        lng = y[i]['geometry']['location']['lng']
        origin = "55.9349405,-3.2151615"
        dest = str(lat) + "," + str(lng)
        stat_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center=Edinburgh,UK&zoom=13&scale=1&size=600x600&maptype=roadmap&key=AIzaSyBzjLAINirGIEr8AaYYzhU7G8bxTgeDbGs&format=png&visual_refresh=true&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C{origin}&markers=size:mid%7Ccolor:0xff0000%7Clabel:2%7C{dest}"
        #resp = requests.get(url=stat_map_url).json()
        #print(resp)
        #polyline_data = resp['routes'][0]['legs'][0]['distance']['text']
        #print(polyline_data)
        #static_map = f'https://maps.googleapis.com/maps/api/staticmap?size=400x400&center={origin}&zoom=4&maptype=roadmap&path=weight:3%7Ccolor:blue%7Cenc:{polyline_data}&key={api_key}'
        s.append((y[i]['name'], y[i]['formatted_address'], stat_map_url))
    return s


def main():
    query = input('Search query: ')
    s = finder(query)
    print(s)


if __name__ == "__main__":
    main()
