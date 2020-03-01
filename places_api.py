import json
import requests

api_key = 'AIzaSyB2i7Jn9JpU1qlHRmTcm0tf_hatN0wLeHM'

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
        stat_map_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={dest}&key={api_key}"
        resp = requests.get(url=stat_map_url).json()
        polyline_data = resp.routes[0].overview_polyline.points
        static_map = f"https://maps.googleapis.com/maps/api/staticmap?markers=size:large|color:red|label:A|latA,longA&markers=size:large|color:red|label:C|latC,longC&markers=size:large|color:red|label:D|latD,longD&markers=size:large|color:red|label:B|latB,longB&path=weight:3|color:red|enc:{polyline_data}&size=300×300&key={api_key}"
        s.append((y[i]['name'], y[i]['formatted_address'], static_map))
    return s


def main():
    query = input('Search query: ')
    s = finder(query)
    print(s)


if __name__ == "__main__":
    main()
