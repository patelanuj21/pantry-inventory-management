import os
from flask import Flask
from dotenv import load_dotenv

parent_path = os.path.abspath('.')
path=f'{parent_path}/.env'
load_dotenv(dotenv_path=path,verbose=True)

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

from backend import routes   