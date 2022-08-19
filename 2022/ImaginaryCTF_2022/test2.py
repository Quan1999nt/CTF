import requests

url = 'http://20.193.247.209:8222/check?name=%22C0loR%22'
myobj = {'name': 'C0loR'}

x = requests.get(url)

#print the response text (the content of the requested file):
print("hello")
print(x.text)
