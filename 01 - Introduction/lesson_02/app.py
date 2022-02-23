from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user")
def vasya1():
    return "<p>Vasya</p>"


@app.route("/test/1")
def test_user1():
    return "<p>Test: Number</br>One</p>"


# lst = [....]
# '<p>' + '</br>'.join(lst) + '</p>'


app.run(debug=True)

# http://127.0.0.1:5000/
# http://127.0.0.1:5000/user
# http://127.0.0.1:5000/test/1
# https://www.google.com/search?q=flask&rlz=1C5CHFA_enUA948UA948&oq=&aqs=chrome.0.69i59i450l7.1672393j0j7&sourceid=chrome&ie=UTF-8

# faker
# pip install faker
