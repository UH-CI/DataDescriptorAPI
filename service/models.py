import datetime
import enum
from flask import g, Flask
from flask_cors import CORS
app = Flask(__name__)

CORS(app,resources={r"/v3/streams/*": {"origins": "*"}},CORS_AUTOMATIC_OPTIONS=True)
