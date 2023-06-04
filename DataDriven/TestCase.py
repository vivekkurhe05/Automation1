# Data Driven Testing using Excel
import os

import requests
import json
from DataDriven import Library

def test_add_multiple_students():
    URL="https://thetestingworldapi.com/api/studentsDetails"
    file=open(os.path.abspath(os.curdir)+"\\Data\\AddStudentDetails.json")
    di=json.loads(file.read())

    obj=Library.Common(os.path.abspath(os.curdir)+"\\test_data.xlsx","Sheet1")
    key_list=obj.fetch_key_names()
    total_rows=obj.fetch_row_count()

    for i in range(2, total_rows+1):
        payload=obj.update_request_with_data(i,di,key_list)
        response=requests.post(URL,payload)
        print(response.text)