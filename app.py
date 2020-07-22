from flask import Flask, render_template, url_for, request, redirect
from database.create_connection import EstablishConnection
# In order to create flask we must first create an instance of the flask class
app = Flask(__name__)

# creating a secret key, personal information so this should be random
# this secret key should then be put into another file that we would import from
app.secret_key = "secret key"

"""
@app.route is a decorator that Flask provides to assign URLs.
The decorator is telling our app that whenever the user enters the "/" domain
then run the index function.
"""


# Here we are creating the web route
# We are sending info from the controller to the 'view' part
"""
By default, GET is the default method if nothing else is explicitly defined.
Here we have added POST method so the user can send a post request with their login credentials.
The code within this function checks to see if the credentials are correct, if so redirecting
the user to the home page
"""

""""
Quiz, multiple choice question, 10 questions, they have a timer in which to do it
We can then generate a feedback score for them.
"""


@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
# This method would allow the message to be displayed on the web route specified
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'AOsborne' or request.form['password'] != 'Password':
            error = 'Invalid Credentials. Please try again.'
        else:
            # this url_for function generates an endpoint for the method
            return redirect(url_for('question'))
    return render_template('login.html', error=error)


@app.route('/python')
def question():
    return render_template('python.html')
    # return "It's time..."


if __name__ == "__main__":
    app.run(debug=True)
