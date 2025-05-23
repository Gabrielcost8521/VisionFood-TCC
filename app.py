from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'visionfood_seguro_123'  # Chave de segurança para sessões

def connect_db():
    return sqlite3.connect('visionfood.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    return redirect(url_for('cadastro'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Erro: este e-mail já está cadastrado."
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['nome'] = user[1]  # Armazena o nome do usuário na sessão
            return redirect(url_for('restaurantes'))
        else:
            return "Credenciais inválidas. Tente novamente."

    return render_template('login.html')

@app.route('/restaurantes')
def restaurantes():
    nome = session.get('nome', 'Usuário')
    return render_template('restaurantes.html', nome=nome)

@app.route('/cameraqr')
def cameraqr():
    return render_template('cameraqr.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

if __name__ == '__main__':
    app.run(debug=True)
