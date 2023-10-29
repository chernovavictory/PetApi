from api import EndToEnd
from data import LoginData

e2e = EndToEnd()
LD = LoginData()



def test_login_delete_user():
    status_code = e2e.login_and_delete()
    assert status_code == 200


