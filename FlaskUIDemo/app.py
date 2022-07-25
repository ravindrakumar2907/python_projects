from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home1')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            #return render_template('home.html')
            #return redirect(url_for('home'))
            return redirect('home')
        #return redirect(url_for('home'))

    return render_template('login.html', error=error)


if __name__ == "__main__":
    print(__name__)
    app.run(debug=True)


"""
Returns a response object (a WSGI application) that, if called, redirects the client to the target location. Supported codes are 301, 302, 303, 305, 307, and 308. 300 is not supported because it's not a real redirect and 304 because it's the answer for a request with a request with defined If-Modified-Since headers.
Params:
location – the location the response should redirect to.
code – the redirect status code. defaults to 302.
Response – a Response class to use when instantiating a response. The default is :class:`werkzeug.wrappers.Response` if unspecified
"""

"""
he Code parameter takes one of following values −

400 − for Bad Request

401 − for Unauthenticated

403 − for Forbidden

404 − for Not Found

406 − for Not Acceptable

415 − for Unsupported Media Type

429 − Too Many Requests
"""