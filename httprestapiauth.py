import requests
my_headers = {'Authorization' : 'Token db4003fb2b8c8b826f36345a5fea7e696e9072ae'}
response = requests.get('http://127.0.0.1:8000/routers/', headers=my_headers)
print(response.content)

PARAMS = {'sapid':'ffff841086ffffffff', 'hostname': 'host_Ray123456', 'loopback': '10.0.0.0', 'type':'AG1' }
response = requests.post(url = 'http://127.0.0.1:8000/routers/', json = PARAMS, headers=my_headers)
print(response.content)

PARAMS = {'sapid':'ffff841086ffffffff', 'hostname': 'host_Ray111111', 'loopback': '10.0.0.0', 'type':'AG1' }
response = requests.put(url = 'http://127.0.0.1:8000/routers/2/', json = PARAMS, headers=my_headers)
print(response.content)

response = requests.delete(url = 'http://127.0.0.1:8000/routers/1/', headers=my_headers)
print(response.content)