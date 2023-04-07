from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from api_mercadopago import payment
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
