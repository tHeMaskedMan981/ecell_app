from rest_framework import serializers
from common.v1 import error_messages
from user.models import User
from common.v1.utils import encryption_utils
from . text_validator import TextValidator
import requests

PASSWORD_CHECKLIST = [
    "text_not_starts_with_whitespace",
    "text_not_ends_with_whitespace",
    "text_contains_atleast_one_number",
    "text_contains_atleast_one_special_character",
    "text_contains_atleast_one_lower_case_chacracter",
    "text_contains_atleast_one_upper_case_chacracter",
]

USER_NAME_CHECKLIST = [
    "text_is_available_in_the_database",
    "text_length_is_atleast_eight",
    "text_not_starts_with_whitespace",
    "text_not_ends_with_whitespace",
    "text_contains_atleast_one_number",
    "text_contains_atleast_one_special_character",
    "text_contains_atleast_one_lower_case_chacracter",
    "text_contains_atleast_one_upper_case_chacracter",
]

STATUS = {
    "ACTIVE": True,
    "INACTIVE": False,
}


class UserRegistartion(object):
    """
    user registeration service
    """

    def __init__(self, user_data):
        # self.user_name = user_data.get('user_name')
        self.email = user_data.get('email')
        self.esummit_id = user_data.get('esummit_id')
        # self.password = user_data.get('password')
        # self.secret_key = pyotp.random_base32()
        self.password_validation_checklist = PASSWORD_CHECKLIST
        self.user_name_validaton_checklist = USER_NAME_CHECKLIST

    # def _get_password_hash(self):
    #     """
    #     set password for the user.
    #     """
    #     return encryption_utils.hash_password(self.password)

    # def _check_password_constrain(self):
    #     return TextValidator(self.password,
    #                          self.password_validation_checklist
    #                          ).check_text()

    # def _check_user_name_constrain(self):
    #     return TextValidator(self.user_name,
    #                          self.user_name_validaton_checklist
    #                          ).check_text()

    def _register_user(self):
        """
        Registers the User.
        """
        data = self._fetch_data()

        # is_user_name_valid = self._check_user_name_constrain()
        # is_password_valid = self._check_password_constrain()
        # if not is_user_name_valid:
        #     raise serializers.ValidationError(error_messages.INVALID_USER_NAME)
        # if not is_password_valid:
        #     raise serializers.ValidationError(error_messages.INVALID_PASSWORD)
        new_user = User.objects.create(
            user_name=data["user_name"],
            email=self.email,
            esummit_id = self.esummit_id,
            profession=data["profession"]
            # password_hash=self._get_password_hash(),
            # secret_key=self.secret_key,
            # status=STATUS["ACTIVE"]
        )
        
        new_user.save()
        return new_user


    def _fetch_data(self):
        """
        Fetches the data of the user from the esummit database based on Esummit ID and the email.
        """
        data = { "esummit_id": self.esummit_id,
                "email": self.email}
        print(data.get('esummit_id'))  
        print(data.get('email'))        
        r = requests.get('https://ecell.in/esummit/get_user_data.php', params = data)
        fetched_data = r.json()
        print (fetched_data["user_name"])
        # if r.status_code == requests.codes.ok:
        if fetched_data["user_name"] is not None:
            print (r.json)
            print (r.text)
            print ("the status code is :" + str(r.status_code))
            return fetched_data
        else : 
            print (r.text)
            print ("the fetch data failed")
            raise serializers.ValidationError(error_messages.USER_NOT_REGISTERED)

        # return {
        #     "user_id": new_user.user_id,
        #     "secret_key": new_user.secret_key,
        #     "email": new_user.email,
        #     "user_name": new_user.user_name
        # }
    

    def _new_user_profile(self, new_user):
        return {
            "user_id": new_user.user_id,
            "esummit_id": new_user.esummit_id,
            "email": new_user.email,
            "user_name": new_user.user_name
        }

    def register_and_get_user_profile(self):
        """
        if user already exists, return its profile. else register a new user and return. 
        """
        new_user = User.objects.filter(
            esummit_id=self.esummit_id, email=self.email).first()
        if new_user is None:
            new_user = self._register_user()
        user_profile = self._new_user_profile(new_user)
        return user_profile

class UserGoogleRegistartion(object):
    """
    user registeration service
    """

    def __init__(self, user_data):
        self.user_name = user_data.get('user_name')
        self.email = user_data.get('email')
        self.photo_url = user_data.get('photo_url')
       
    def _register_user(self):
        """
        Registers the User.
        """
        print("making new user")

        new_user = User.objects.create(
            user_name=self.user_name,
            email=self.email,
            photo_url=self.photo_url
        )
        
        new_user.save()
        # print("new user made: " + new_user)
        return new_user

    def _new_user_profile(self, new_user):
        return {
            "user_id": new_user.user_id,
            "esummit_id": new_user.esummit_id,
            "email": new_user.email,
            "photo_url": new_user.photo_url,
            "user_name": new_user.user_name
        }

    def register_and_get_user_profile(self):
        """
        if user already exists, return its profile. else register a new user and return. 
        """
        new_user = User.objects.filter(
            user_name=self.user_name, email=self.email).first()
        if new_user is None:
            new_user = self._register_user()
        user_profile = self._new_user_profile(new_user)
        print (user_profile)
        return user_profile
