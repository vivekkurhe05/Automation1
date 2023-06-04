import json
import jsonpath
import requests
import os

def test_add_new_student():
    global id
    URL="https://thetestingworldapi.com/api/studentsDetails"
    file=open(os.path.abspath(os.curdir)+"\\Data\\RequestJson.json")
    payload_request=json.loads(file.read())
    response=requests.post(URL, payload_request)
    id=jsonpath.jsonpath(response.json(),"id")
    print(id[0])

def test_get_details():
    URL="https://thetestingworldapi.com/api/studentsDetails"+str(id[0])
    response=requests.get(URL)
    print(response.text)