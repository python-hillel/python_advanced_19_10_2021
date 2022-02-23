import requests
from flask import Flask
from flask import jsonify

# from random import choices
# from string import ascii_lowercase

from utils import generator_random_string

from webargs import fields, validate
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.errorhandler(400)
@app.errorhandler(422)
def handle_error(err):
    headers = err.data.get('headers')
    messages = err.data.get('messages', ['Invalidate value'])
    if headers:
        return jsonify({'errors': messages}, err.code, headers)
    else:
        return jsonify({'errors': messages}, err.code)


@app.route('/str')
@use_kwargs(
    {
        'length': fields.Int(
            required=True,
            # missing=10,
            validate=[validate.Range(min=1, max=100)]
        )
    },
    location='query'
)
def get_random_string(length):
    # length = request.args.get('l', '10')
    # if length.isdigit():
    #     length = int(length)
    # else:
    #     # return 'Error incorrect param.'
    #     return Response('Error incorrect param.', status=400)

    return '<h3>' + generator_random_string(length) + '</h3>'


app.run(debug=True, port=8000)


# requests, json
# response = requests.get('google.com')
# print(response.text)
# print(response.json())
