
import requests
import json


URL = "http://127.0.0.1:8000/stuinfo/"

def get_id(id=None):
    data= {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url= URL,data = json_data)    
    data = r.json()
    print(data)
    
# get_id()


def post_create():
    data = {
        'name': 'Ramhari',
        'age' : 45,
        'address': 'Lumbini'

    }
    json_data = json.dumps(data)
    r = requests.post(url= URL,data = json_data)
    data = r.json()
    print(data)
# post_create()

def post_update():
    data = {
        'id': 3,
        'name': 'Ramhari',
        'age' : 45,
        'address': 'Lumbini'

    }
    json_data = json.dumps(data)
    r = requests.update(url= URL,data = json_data)
    data = r.json()
    print(data)


