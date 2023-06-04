import requests
import json
import os
import pytest

@pytest.fixture(scope="module")
def setup():
    global BASE_URL
    BASE_URL="https://thetestingworldapi.com"


def test_add_student_data(setup):
    global student_id
    URL=BASE_URL+"/api/studentsDetails"
    file=open(os.path.abspath(os.curdir)+"\\Data\\RequestJson.json")
    di=json.loads(file.read())
    response=requests.post(URL,di)
    pi_res=json.loads(response.text)
    student_id=pi_res["id"]
    print(student_id)
    assert response.status_code == 201

def test_get_student_data(setup):
    URL=BASE_URL+"/api/studentsDetails/"+str(student_id)
    response=requests.get(URL)
    di=json.loads(response.text)
    assert di["data"]["id"] == student_id

def test_update_student_data(setup):
    URL=BASE_URL+"/api/studentsDetails/"+str(student_id)
    payload = {
        "id": student_id,
        "first_name": "Vivek",
        "middle_name": "Mahendra",
        "last_name": "Kurhe",
        "date_of_birth": "05/11/1993"
    }
    response=requests.put(URL, payload)
    di=json.loads(response.text)
    assert di["msg"] == "update  data success"

def test_delete_student_data(setup):
    URL = BASE_URL+"/api/studentsDetails/"+str(student_id)
    response=requests.delete(URL)
    di=json.loads(response.text)
    assert di["msg"] == "Delete  data success"