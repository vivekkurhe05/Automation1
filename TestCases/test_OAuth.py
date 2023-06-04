import requests
import json

def test_oauth_api():
    token_url="https://thetestingworldapi.com/Token"
    data = {
        "grant_type":"password",
        "username":"admin",
        "password":"adminpass"
    }
    response=requests.post(token_url, data)
    token_res=json.loads(response.text)
    access_token=token_res["access_token"]
    auth={
        "Authorization": "Bearer "+access_token
    }
    URL="https://thetestingworldapi.com/api/stDetails/1104"
    response=requests.get(URL, headers=auth) # pass auth as dictionary
    print(response.text)