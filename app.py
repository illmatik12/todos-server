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

#DB
import pymysql

import json


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
        # self.item_query();
        todos = self.item_query();
        return jsonify(todos)
        # return todos


    def item_query(self):

        conn = pymysql.connect(
            user='test',
            passwd='test1234',
            host='localhost',
            db='testdb',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

        # value1 = request.form['item_id']
        # print("request value : " , value1 )

        # user_sql = "select * from user where id = " + str(value1)
        user_sql = "select name from user "
        with conn:
            cur = conn.cursor()
            cur.execute(user_sql)
            rows = cur.fetchall()


        # json_return = json.dumps(rows)

        # print(json_return)

        return rows

#api
api.add_resource(todo_item, '/todos')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
