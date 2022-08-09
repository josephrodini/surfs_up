#dependency
from flask import Flask

# create a new flask app instance
app = Flask(__name__)

# Define the root (starting point)
@app.route('/')

# hello world function
def hello_world():
    return 'Hello world'