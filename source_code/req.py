import requests

r = requests.post("http://0.0.0.0:5000/", json={'ID':'10078'})
print(r.status_code, r.reason)
print(r.text)
