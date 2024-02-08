#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/2/3 10:06
# @Author : changxy


from flask import Flask, request, json, jsonify
from flask.json import loads

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route("/user/<name>")
def get_user(name):
    if name == 'xy':
        u_id = 1
    else:
        u_id = 2
    return jsonify({"id": u_id})


@app.route("/age")
def get_age():
    user_id = request.args['id']
    age = 100 if user_id == 1 else 101
    return jsonify({"age": age})


@app.route("/openapi")
def get_api():
    return loads("""
            {"openapi":"3.1.0","info":{"title":"demo","description":"","version":"1.0.0"},"tags":[],"paths":{"http://127.0.0.1:2020/user/{name}":{"get":{"summary":"通过用户名称查询用户id","deprecated":false,"description":"","tags":[],"parameters":[{"name":"name","in":"path","description":"","required":true,"schema":{"type":"number"}}],"responses":{"200":{"description":"成功","content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"ID 编号"}},"required":["id"]}}}}},"security":[]}},"http://127.0.0.1:2020/age":{"get":{"summary":"通过用户id查询用户年龄","deprecated":false,"description":"","tags":[],"parameters":[{"name":"id","in":"query","description":"","required":false,"schema":{"type":"number"}}],"responses":{"200":{"description":"成功","content":{"application/json":{"schema":{"type":"object","properties":{"age":{"type":"number"}}}}}}},"security":[]}}},"components":{"schemas":{},"securitySchemes":{}},"servers":[]}  
        """)


if __name__ == "__main__":
    app.run(port=2020, host="127.0.0.1", debug=True)
