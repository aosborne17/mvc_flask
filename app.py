from flask import Flask

# In order to create flask we must first create an instance of the flask class
app = Flask(__name__)

"""
@app.route is a decorator that Flask provides to assign URLs.
The decorator is telling our app that whenever the user enters the "/" domain
then run the index function.
"""


# Here we are creating the web route
# We are sending info from the controller to the 'view' part
@app.route("/")
# This method would allow the message to be displayed on the web route specified
def index():
    return "<h1>Welcome to MVC with Flask Project</h1>"


@app.route("/<username>")
def welcome_user(username):
    return "<h1>Welcome to the Python Flask App {} </h1>".format(username)


# @app.route("/andrew")
# def welcome_user():
#     return "<h1>Welcome to the Python Flask App Andrew</h1>"


if __name__ == "__main__":
    app.run(debug=True)
