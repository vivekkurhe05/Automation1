import requests
import json
import os
import pytest

@pytest.fixture(scope="module")
def setupdata():
    global BASE_URL
    BASE_URL="https://thetestingworldapi.com"

def test_add_new_data(setupdata):
    URL=BASE_URL+"/api/studentsDetails"
    file=open(os.path.abspath(os.curdir)+"\\Data\\RequestJson.json")
    di=json.loads(file.read())
    response=requests.post(URL,di)
    pi=json.loads(response.text)
    student_id=pi["id"]
    assert response.status_code == 201

    URL=BASE_URL+"/api/technicalskills"
    file=open(os.path.abspath(os.curdir)+"\\Data\\TechnicalSkills.json")
    di=json.loads(file.read())
    di["id"]=student_id
    di["st_id"]=student_id
    response=requests.post(URL,di)
    assert response.status_code == 200

    URL = BASE_URL + "/api/addresses"
    file = open(os.path.abspath(os.curdir) + "\\Data\\Address.json")
    di = json.loads(file.read())
    di["stId"] = student_id
    response = requests.post(URL, di)
    assert response.status_code == 200

    URL = BASE_URL + "/api/FinalStudentDetails/"+str(student_id)
    response = requests.get(URL, di)
    print(response.text)

