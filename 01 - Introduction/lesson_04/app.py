from flask import Flask
from faker import Faker

from webargs import fields, validate
from webargs.flaskparser import use_kwargs

from lesson_04.utils import get_students_list
from lesson_04.formater import list2htmlBR


app = Flask(__name__)


# dns_name/students  cnt=10
@app.route('/students')
@use_kwargs(
    {
        'cnt': fields.Int(
            required=True,
            validate=[validate.Range(min=1, max=15)]
        )
    },
    location='query'
)
def students(cnt):
    # f = Faker()
    # lst = []
    # for i in range(cnt):
    #     lst.append(f.name())

    # s = '<br>'.join(get_students_list(cnt))

    return list2htmlBR(get_students_list(cnt))





app.run(debug=True)
