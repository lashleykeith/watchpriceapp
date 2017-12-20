from flask import Flask
from src.common.database import Database

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123"

@app.before_first_request
def init_db():
    Database.initialize()

from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/user")


'''
92
Lecutre
To use mail gun
import requests
r = requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
        data={"from": "Excited User <excited@samples.mailgun.org>",
              "to": ["johnik.va@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})
r.content
b'{\n  "message": "Great job! To send a real email please create an account here: https://app.mailgun.com/signup"\n}'



'''

