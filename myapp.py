# import flask
from flask import Flask

# main app
app = Flask(__name__)

# set route untuk /
@app.route("/")
# function index
def index():
    # print text
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)