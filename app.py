# -- coding: utf-8 --


from datetime import datetime


from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import jsonify

from flask_cors import CORS


from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import logging

logging.getLogger('flask_cors').level = logging.DEBUG


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# auth = HTTPBasicAuth()

CORS(app)


users = {
        "semi": generate_password_hash("love")
}
todos = [{
    "name": "청소"
},
    {
        "name": "블로그 쓰기"
},
    {
        "name": "밥먹기"
},
    {
        "name": "안녕"
    },
    {
        "name": "Hello Semi"
    }
]

api = Api(app)


class todo_item(Resource):
    def get(self):
        return jsonify(todos);

#api
api.add_resource(todo_item, '/todos')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
