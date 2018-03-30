# -*- coding: UTF-8 -*-

from flask import Flask, jsonify, request, url_for, render_template, redirect, abort
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def getHome():
    return jsonify({'name': 'fox'})


@app.route('/page')
def render():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>你好</h1>
    <script src="{{ url_for('static', filename='index.js') }}"></script>
</body>
</html>"""


@app.route('/template')
def renderTem():
    return render_template(
        'index.html', name=url_for('static', filename='index.js'))


@app.route('/a')
def a():
    return redirect(url_for('b'))


@app.route('/b')
def b():
    abort(401)
    return 'this is b page'


app.run()
