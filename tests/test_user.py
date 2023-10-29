import pytest
import json
import requests


from api import User
from data import LoginData

user = User()
LD = LoginData()


@pytest.mark.parametrize(('email','password', 'expected_result'),
                         [(LD.VALID_EMAIL, LD.VALID_PASSWORD, 200),
                          (LD.INVALID_EMAIL, LD.VALID_PASSWORD,400),
                          (LD.VALID_EMAIL, LD.INVALID_PASSWORD, 400),
                          ])
def test_login(email, password, expected_result):
    data = {
        "email": email,
        "password": password
    }
    response = requests.post("http://34.141.58.52:8000/" + "login", data=json.dumps(data))

    status_code = response.status_code
    assert status_code == expected_result



def test_user_id():
    res = user.get_user_id()
    status_code = res[1]
    user_id = res[0]
    assert user_id
    assert status_code == 200



def test_registration():
    res = user.registration()
    user_token = res[0]
    user_id = res[1]
    status_code = res[2]
    assert status_code == 200
    assert user_token and user_id



def test_delete():
    status_code = user.delete()
    assert status_code == 200