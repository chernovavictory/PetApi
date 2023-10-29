import json
import requests
import uuid



from data import LoginData


# from dotenv import load_dotenv
""""Устанавливаем пакет .env"""

#load_dotenv()
LD = LoginData()



class Pets:
    """Апи библиотека для сайта url=http://34.141.58.52:8080/#/ """
    def __init__(self):
        self.base_url = "http://34.141.58.52:8000/"


    def login_user(self) -> json:
        data = {
            "email": LD.VALID_EMAIL,
            "password": LD.VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        user_token = response.json()["token"]
        user_id = response.json()["id"]
        status_code = response.status_code
        return user_token, user_id, status_code



    def create_pet(self) ->json:
        user_id = self.login_user()[1]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        data = {
              "name": "Honey",
              "type": "hamster",
              "age": 3,
              "gender": "Female",
              "owner_id": user_id,
            }
        response = requests.post(self.base_url + "pet", data=json.dumps(data), headers=headers)
        pet_id = response.json()["id"]
        status_code = response.status_code
        return pet_id, status_code


    def put_like(self) -> json:
        user_token = self.login_user()[0]
        pet_id = self.create_pet()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status_code = res.status_code
        return status_code


    def put_comment(self) -> json:
        pet_id = self.create_pet()[0]
        user_id = self.login_user()[1]
        user_name = LD.VALID_EMAIL
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        data = {
            "pet_id": pet_id,
            "message": "cooool",
            "user_id": user_id,
            "user_name": user_name,
        }
        response = requests.put(self.base_url + f"pet/{pet_id}/comment", data=json.dumps(data), headers=headers)
        comment_id = response.json()
        status_code = response.status_code
        return comment_id, status_code


    def get_pet_info(self) -> json:
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.get(self.base_url + f"pet/{pet_id}", headers=headers)
        pet_id = response.json()["pet"]["id"]
        pet_owner_id = response.json()["pet"]["owner_id"]
        pet_owner_name = response.json()["pet"]["owner_name"]
        pet_name = response.json()["pet"]["name"]
        pet_age = response.json()["pet"]["age"]
        pet_type = response.json()["pet"]["type"]
        pet_gender = response.json()["pet"]["gender"]
        pet_pic = response.json()["pet"]["pic"]
        pet_liked_by_user = response.json()["pet"]["liked_by_user"]
        pet_likes_count = response.json()["pet"]["likes_count"]
        pet_comments = response.json()["comments"]
        status_code = response.status_code
        return pet_id, status_code, pet_comments
            # pet_owner_id, pet_owner_name, pet_name, pet_age, pet_type, pet_gender, pet_pic, pet_liked_by_user, pet_likes_count


    def get_pets_list(self) -> json :
        user_id = self.login_user()[1]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        data = {
            "user_id": user_id,
        }
        response = requests.post(self.base_url + "pets", data=json.dumps(data), headers=headers)
        list_pets = response.json()["list"]
        count_pets = response.json()["total"]
        status_code = response.status_code
        return list_pets, count_pets, status_code


    def change_pet_info(self) -> json:
        pet_id = self.create_pet()[0]
        user_id = self.login_user()[1]
        user_name = LD.VALID_EMAIL
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        data = {
            "pet_id": pet_id,
            "name": "PyTest",
            "type": "cat",
            "owner_id": user_id,
            "owner_name": user_name,
            "liked_by_user": "false",
        }
        response = requests.patch(self.base_url + "pet", data=json.dumps(data), headers=headers)
        pet_id = response.json()["id"]
        status_code = response.status_code
        return pet_id, status_code


    def post_image(self):
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        files = {'pic': ('cat.jpg', open('tests/photo/cat.jpg', 'rb'), 'image/jpg')}
        response = requests.post(self.base_url + f"pet/{pet_id}/image", headers=headers, files=files)
        link = response.json()
        status_code = response.status_code
        return link, status_code


    def delete_pet(self) -> json :
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f"pet/{pet_id}", headers=headers)
        status_code = response.status_code
        return status_code




class User:
    def __init__(self):
        self.base_url = "http://34.141.58.52:8000/"



    def login(self) -> json:
        data = {
            "email": LD.VALID_EMAIL,
            "password": LD.VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        user_token = response.json()["token"]
        user_id = response.json()["id"]
        status_code = response.status_code
        return user_token, user_id, status_code



    def get_user_id(self) -> json:
        user_token = self.login()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.get(self.base_url + "users", headers=headers)
        user_id = response.json()
        status_code = response.status_code
        return user_id, status_code


    def registration(self) -> json:
        email = uuid.uuid4().hex
        data = {
            "email": f"{email}@gmail.com",
            "password": "1234",
            "confirm_password": "1234"
        }

        response = requests.post(self.base_url + "register", data=json.dumps(data))
        token = response.json()["token"]
        user_id = response.json()["id"]
        status_code = response.status_code
        return token, user_id, status_code


    def delete(self) -> json:
        """Delete after login"""
        user_id = self.login()[1]
        user_token = self.login()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f"users/{user_id}", headers=headers)
        status_code = response.status_code
        return status_code





class EndToEnd:
    def __init__(self):
        self.base_url = "http://34.141.58.52:8000/"


    def registration_and_delete(self) -> json:
        email = uuid.uuid4().hex
        data = {
            "email": f"{email}@gmail.com",
            "password": "1234",
            "confirm_password": "1234"
        }

        response = requests.post(self.base_url + "register", data=json.dumps(data))
        token = response.json()["token"]
        user_id = response.json()["id"]
        headers = {"Authorization": f'Bearer {token}'}
        params = {"id": user_id}
        response = requests.delete(self.base_url + f"users/{user_id}", headers=headers, params = params)
        status_code = response.status_code
        return status_code


    def login_and_delete(self) -> json:
        data = {
            "email": LD.VALID_EMAIL,
            "password": LD.VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        user_token = response.json()["token"]
        user_id = response.json()["id"]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f"users/{user_id}", headers=headers)
        status_code = response.status_code
        return status_code


    def create_full_pet(self) -> json:
        """login"""
        data_login = {
            "email": LD.VALID_EMAIL,
            "password": LD.VALID_PASSWORD
        }
        response_login = requests.post(self.base_url + "login", data=json.dumps(data_login))
        user_token = response_login.json()["token"]
        user_id = response_login.json()["id"]
        status_login = response_login.status_code

        """create pet"""
        headers = {"Authorization": f'Bearer {user_token}'}
        data_create = {
            "name": "Honey",
            "type": "hamster",
            "age": 3,
            "gender": "Female",
            "owner_id": user_id,
        }
        response_create = requests.post(self.base_url + "pet", data=json.dumps(data_create), headers=headers)
        pet_id = response_create.json()["id"]
        status_create = response_create.status_code

        """add a photo to the pet"""
        files = {'pic': ('cat.jpg', open('/Users/v/PycharmProjects/PetApi/tests/photo/cat.jpg', 'rb'), 'image/jpg')}
        response_photo = requests.post(self.base_url + f"pet/{pet_id}/image", headers=headers, files=files)
        status_photo = response_photo.status_code
        # link = response_photo.json()

        """put like"""
        response_like = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status_like = response_like.status_code
        # status_like_str = (str(status_like))
        # print("Код ответа для лайка =" + status_like_str)

        """put comment"""
        user_name = LD.VALID_EMAIL
        data_comment = {
            "pet_id": pet_id,
            "message": "cooool",
            "user_id": user_id,
            "user_name": user_name,
        }
        response_comment = requests.put(self.base_url + f"pet/{pet_id}/comment", data=json.dumps(data_comment), headers=headers)
        status_comment = response_comment.status_code

        """change pet info"""
        data_change_pet = {
            "id": pet_id,
            "name": "PyTest",
            "type": "cat"
        }
        response_change = requests.patch(self.base_url + "pet", data=json.dumps(data_change_pet), headers=headers)
        status_change = response_change.status_code
        pet_id_change = response_change.json()["id"]

        """delete pet"""
        response_delete_pet = requests.delete(self.base_url + f"pet/{pet_id}", headers=headers)
        status_delete = response_delete_pet.status_code
        return status_login, status_create, status_photo, status_like, status_comment, status_delete, status_change

# for i in range(2):
#     EndToEnd().create_full_pet()












# Pets().login_user()
# Pets().create_pet()
# Pets().put_like()
# Pets().put_comment()
# Pets().get_pet_info()
# #Pets().get_pets_list()
# Pets().change_pet_info()
# Pets().post_image()
# Pets().delete_pet()


# User().login()
# User().get_user_id()
# User().registration()
# User().delete()


# EndToEnd().registration_and_delete()
# EndToEnd().login_and_delete()
# EndToEnd().create_full_pet()
