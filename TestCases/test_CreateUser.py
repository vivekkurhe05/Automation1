import requests
import pytest

# API URL
url = "https://reqres.in/api/users"


@pytest.fixture(scope="module")
def setup_data():
    global request_body

    # request_body is local to this method, hence declaring global makes it accessible throughout the file
    request_body = {
        "name": "Vivek",
        "job": "QA Lead"
    }

def test_create_new_user(setup_data):
    # Make POST request with Json input body
    response=requests.post(url,request_body)
    # Validating response code
    assert response.status_code == 201

@pytest.mark.skip
def test_create_other_user(setup_data):
    # Make POST request with Json input body
    response=requests.post(url,request_body)
    # Validating response code
    assert response.status_code == 201