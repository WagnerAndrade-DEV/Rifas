from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from api_mercadopago import payment
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/200-no-pix', methods=['GET', 'POST'])
def premio1():

    if request.method == 'POST':

        name = 'R$200,00 no PIX'
        price = 0.50
        quantidad = request.form.get('quantidade')
        quantidade = int(quantidad)

        nome = request.form['nome']
        telefone = request.form['telefone']
        data = datetime.today()

        conn = sqlite3.connect('sorteios.db')
        cursor = conn.cursor()

        cursor.execute(f'''
                INSERT INTO sorteio (nome, telefone, data, sorteio)
                VALUES ('{nome}', '{telefone}', '{data}', '200noPIX')
            ''')

        conn.commit()
        conn.close()

        return redirect(payment(request, name=name, quantity=quantidade, price=price))

    return render_template("sorteio1.html")


@app.route('/1000-no-pix', methods=['GET', 'POST'])
def premio2():

    if request.method == 'POST':

        name = 'R$1000,00 no PIX'
        price = 2.50
        quantidad = request.form.get('quantidade')
        quantidade = int(quantidad)

        nome = request.form['nome']
        telefone = request.form['telefone']
        data = datetime.today()

        conn = sqlite3.connect('sorteios.db')
        cursor = conn.cursor()

        cursor.execute(f'''
                INSERT INTO sorteio (nome, telefone, data, sorteio)
                VALUES ('{nome}', '{telefone}', '{data}', '1000noPIX')
            ''')

        conn.commit()
        conn.close()

        return redirect(payment(request, name=name, quantity=quantidade, price=price))

    return render_template("sorteio2.html")


@app.route('/iphone', methods=['GET', 'POST'])
def premioPrincipal():

    if request.method == 'POST':

        name = 'Iphone 13 (128 GB)'
        price = 9.99
        quantidad = request.form.get('quantidade')
        quantidade = int(quantidad)

        print(quantidade)

        nome = request.form['nome']
        telefone = request.form['telefone']
        data = datetime.today()

        conn = sqlite3.connect('sorteios.db')
        cursor = conn.cursor()

        cursor.execute(f'''
                INSERT INTO sorteio (nome, telefone, data, sorteio)
                VALUES ('{nome}', '{telefone}', '{data}', 'iphone13')
            ''')

        conn.commit()
        conn.close()


        return redirect(payment(request, name=name, quantity=quantidade, price=price))

    return render_template("principal.html")


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True)
