import json
import requests

URL='http://127.0.0.1:8000/student/'
headers = {"Content-Type": "application/json; charset=utf-8"}
def get_student(pk=None):
    if pk is not None:
       res= requests.get(url=URL+str(pk)+'/',headers=headers)
       data= res.json()
       return data
    res = requests.get(url=URL)
    data = res.json()
    return data

def post_student():
    data={'email':'nisssf@gmail.com','password':'83838'}
    jsondata=json.dumps(data)
    res= requests.post(url=URL,headers=headers,data=jsondata)
    data = res.json()
    return data

def delete_student(pk):
    res= requests.delete(url=URL+str(pk)+'/',headers=headers)
    data = res.json()
    return data

def update_student(pk):
    data ={'id':pk,'password':'12344333'}
    jsondata= json.dumps(data)
    res = requests.patch(url=URL+str(pk)+'/',headers=headers,data=jsondata)
    data = res.json()
    return data


print(delete_student(16))