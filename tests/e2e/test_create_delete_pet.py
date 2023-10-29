import pytest


from api import EndToEnd
from data import LoginData

e2e = EndToEnd()
LD = LoginData()


def test_create_full_pet():
    res = e2e.create_full_pet()
    login = res[0]
    create_pet = res[1]
    add_photo = res[2]
    add_like = res[3]
    add_comment = res[4]
    delete = res[5]
    change_info = res[6]
    assert login == 200
    assert create_pet == 200
    assert add_photo == 200
    assert add_like == 200
    assert add_comment == 200
    assert change_info == 200
    assert delete == 200

