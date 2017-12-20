import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):

        user_data = Database.find_one("users", {"email": email}) # Password in sha512 -> pbkdf2_sha512
        if user_data is None:
            raise UserErrors.UserNotExistsError("Your user does")
        if Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True