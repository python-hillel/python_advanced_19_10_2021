from flask import Flask

from lesson_08.db import execute_query
from formater import list_rec2html_br

from webargs import fields, validate
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


@app.route('/customers')
@use_kwargs(
    {
        'first_name': fields.Str(
            required=False,
            missing=None,
        ),
        'last_name': fields.Str(
            required=False,
            missing=None,
        )
    },
    location='query'
)
def get_customers(first_name, last_name):
    sql = 'select FirstName, PhoneNumber from customers'
    # if first_name:
    #     sql = f'select * from customers where FirstName = "{first_name}"'

    where_filter = {}
    if first_name:
        where_filter['FirstName'] = first_name

    if last_name:
        where_filter['LastName'] = last_name

    if where_filter:
        # sql += ' where ' + ' or '.join(f'{k} = "{v}"' for k, v in where_filter.items())
        sql += ' where ' + ' or '.join(f'{k} = ?' for k, v in where_filter.items())
        params = [v for k, v in where_filter.items()]

    records = execute_query(sql, params)

    return list_rec2html_br(records)


app.run(debug=True, port=8080, host='0.0.0.0')
