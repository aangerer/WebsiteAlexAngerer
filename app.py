rom flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['DEBUG'] = True
