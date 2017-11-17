import json
import os

import pymysql.cursors
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

os.environ["NLS_LANG"] = "GREEK_GREECE.AL32UTF8"
db = SQLAlchemy(app)


# toolbar = DebugToolbarExtension(app)

@app.route('/query', methods=['POST'])
def test1():
    print(json.dumps(request.json, indent=4))
    body = request.json
    # Connect to the database
    connection = pymysql.connect(host=body['host'],
                                 user=body['user'],
                                 password=body['password'],
                                 db=body['db'],
                                 charset=body['charset'],
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = body['query']
            cursor.execute(sql)
            result = cursor.fetchmany(100)
    finally:
        connection.close()
    return jsonify(result)
