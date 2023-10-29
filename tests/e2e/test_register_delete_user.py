from api import EndToEnd
from data import LoginData

e2e = EndToEnd()
LD = LoginData()



def test_register_delete_user():
    for i in range(2):
        status_code = e2e.registration_and_delete()
        assert status_code == 200
        print(f"Статус код: {status_code}")
