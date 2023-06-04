import jsonpath
import requests
import json

# API URL
url = "https://reqres.in/api/users/7"

def test_fetch_user_details():
    response = requests.get(url)
    json_response=json.loads(response.content)
    first_name = jsonpath.jsonpath(json_response, "data.first_name")
    assert first_name[0] == "Michael"

