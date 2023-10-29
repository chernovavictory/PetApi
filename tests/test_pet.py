import pytest
import json
import requests

from api import Pets
from data import LoginData
from data import PetInfo


pet = Pets()
LD = LoginData()
PI = PetInfo()




# Проверка на два параметра: позитивный сценарий и негативный сценарий (токен неверный, ошибка авторизации)
@pytest.mark.parametrize(('name', 'expected_result', 'user_token', 'owner_id'),
                         [(PI.VALID_NAME, 200, pet.login_user()[0], pet.login_user()[1]),
                          (PI.VALID_NAME, 401, LD.INVALID_TOKEN, pet.login_user()[1]),
                          (PI.VALID_NAME, 200, pet.login_user()[0], LD.INVALID_OWNER_ID),
                          ])
def test_create_pet(name, expected_result, user_token, owner_id):
    headers = {"Authorization": f'Bearer {user_token}'}
    data = {
        "name": name,
        "type": "hamster",
        "age": 3,
        "gender": "Female",
        "owner_id": owner_id,
    }
    response = requests.post("http://34.141.58.52:8000/" + "pet", data=json.dumps(data), headers=headers)

    status_code = response.status_code
    assert status_code == expected_result




def test_put_like():
    status_code = pet.put_like()
    assert status_code == 200



def test_put_comment():
    res = pet.put_comment()
    comment_id = res[0]
    status_code = res[1]
    assert comment_id
    assert status_code == 200



def test_get_pet_info():
    for i in range(2):
        res = pet.get_pet_info()
        pet_id = res[0]
        pet_comments = res[2]
        status_code = res[1]
        assert type(pet_comments) == list
        assert pet_id
        assert status_code == 200
        print(f"Статус код получения информации о питомце: {status_code}")



def test_get_pets_list():
    res = pet.get_pets_list()
    list_pets = res[0]
    count_pets = res[1]
    status_code = res[2]
    assert list_pets
    assert count_pets
    assert status_code == 200



def test_change_pet_info():
    res = pet.change_pet_info()
    pet_id = res[0]
    status_code = res[1]
    assert pet_id
    assert status_code == 200



def test_delete_pet():
    status_code = pet.delete_pet()
    assert status_code == 200