from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Conectar ao banco de dados SQLite
def connect_db():
    return sqlite3.connect('visionfood.db')

# Criar a tabela se não existir
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

# Executa a criação da tabela ao iniciar
create_table()

# Rota inicial redireciona para /cadastro
@app.route('/')
def index():
    return redirect(url_for('cadastro'))

# Rota de cadastro
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

# Rota de login
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
            return redirect(url_for('home'))
        else:
            return "Credenciais inválidas. Tente novamente."

    return render_template('login.html')

# Página após login
@app.route('/home')
def home():
    return "<h1 style='text-align:center; font-family:Arial;'>Login realizado com sucesso!<br>Bem-vindo ao VisionFood</h1>"

if __name__ == '__main__':
    app.run(debug=True)
