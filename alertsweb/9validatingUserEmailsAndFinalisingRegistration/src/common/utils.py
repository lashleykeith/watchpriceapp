from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\W-]+@([\W-]+\.)+[\W]+$')
        return True if email_address_matcher(email) else False



    @staticmethod
    def hash_password(password):

        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Password
        :param hashed_password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512-hashed password
        :return:
        """

        return pbkdf2_sha512.verify(password, hashed_password)