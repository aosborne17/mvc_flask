from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

from database.create_connection import EstablishConnection
# In order to create flask we must first create an instance of the flask class
app = Flask(__name__)

# creating a secret key, personal information so this should be random
# this secret key should then be put into another file that we would import from
"""
To import a random secret, we must first import the secrets module in the terminal
and do secrets.token_hex(16) which will give a random 16 character string
"""
app.secret_key = '397db8358c85c670a7b967bff7d0f82f'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating a DB instance, which allows us to work with our database
# Which alchemy we can represent database structure as classes
# these classes are referred to as 'models'
# each class will be it's own table in the database

# db = SQLAlchemy(app)
#
#
# class User(db.model):
#     # here we have set the primary id, and it is an int type and it is also the primary key
#     id = db.column(db.Integer, primary_key=True)
#     # here we have created the username column which is a string but can only be 20 characters, and cannot be null
#     username = db.column(db.String(20), unique=True, nullable=False)
#     password = db.column(db.String(60), nullable=False)
#
#     # this is a magic method that represents how the object will look like when we print a user object
#     def __repr__(self):
#         return "User: {}".format(self.username)

# Now that this class has been created, we can use the command line to create the db


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
    if 'username' in session:
        username = session['username']
    return render_template('welcome.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
# This method would allow the message to be displayed on the web route specified
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'AOsborne' or request.form['password'] != 'Password':
            error = 'Invalid Credentials. Please try again.'
        else:
            # this url_for function generates an endpoint for the method
            return redirect(url_for('question'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('welcome'))


@app.route('/python')
def question():
    return render_template('python.html')


if __name__ == "__main__":
    app.run(debug=True)
