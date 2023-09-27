#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Simple echo application</title>
        </head>
        <body>
            <h1> Hello there! write here your name </h1>
            <form action="/echo_user_input" method="POST">
                <input name="user_input">
                <input type="submit" value="Submit!">
            </form>
        </body>
    </html>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "Hello " + input_text + ", pleased to meet you!"