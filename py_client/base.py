import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
# endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint,params= {"abc":34} , json={'query':'hello world'}) # API - application programming interface


get_response = requests.post(endpoint, json={"title": "hello world"})
# get_response = requests.get(endpoint,params={"abc": 123}, json={"product_id": 123})
# print(get_response.text) #print raw text response
print(get_response.json()) #print raw text response

# HTTP request = HTML
# rest API HTTP request =JSON
# JSON(JavaScript Object Notaion) ~ python dictionary
# print(get_response.status_code)