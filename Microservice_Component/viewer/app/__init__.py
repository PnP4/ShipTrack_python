from flask import Flask

app = Flask(__name__)

from app import tasks, data_view