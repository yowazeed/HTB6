# Python program to get a set of 
# places according to your search 
# query using Google Places API 

# importing required modules 
import requests, json 

# enter your api key here 
api_key = 'AIzaSyB2i7Jn9JpU1qlHRmTcm0tf_hatN0wLeHM'

# url variable store url 
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search 

def finder(query):
    # get method of requests module 
    # return response object 
    r = requests.get(url + 'query=' + query +'&key=' + api_key) 
    # json method of response object convert 
    # json format data into python format data 
    x = r.json() 
    # now x contains list of nested dictionaries 
    # we know dictionary contain key value pair 
    # store the value of result key in variable y 
    y = x['results'] 
    # keep looping upto length of y 
    #print(y)
    s = []
    for i in range(len(y)): 	
    	# Print value corresponding to the 
    	# 'name' key at the ith index of y 
        #print(y[i][ 'formatted_address'])
        s.append((y[i][ 'name'], y[i][ 'formatted_address']))
    return s

def main():
    query = input('Search query: ') 
    s =finder(query)
    print(s)

main()