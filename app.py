from flask import Flask, render_template, url_for, request, redirect

# In order to create flask we must first create an instance of the flask class
app = Flask(__name__)

"""
@app.route is a decorator that Flask provides to assign URLs.
The decorator is telling our app that whenever the user enters the "/" domain
then run the index function.
"""


# Here we are creating the web route
# We are sending info from the controller to the 'view' part
@app.route('/', methods=['GET', 'POST'])
# This method would allow the message to be displayed on the web route specified
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'AOsborne' or request.form['password'] != 'Password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/home'))
    return render_template('base.html', error=error)


@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
