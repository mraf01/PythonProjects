from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Per gestire la sessione


users = {
    'Mario': {
        'password': 'password123',
        'ordini_in_corso': ['Ordine 1', 'Ordine 2'],
        'ordini_vecchi': ['Ordine 3', 'Ordine 4']
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('personal'))
        else:
            return 'Login fallito, riprova'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = {'password': password, 'ordini_in_corso': [], 'ordini_vecchi': []}
            return redirect(url_for('index'))
        else:
            return 'Utente già registrato'
    return render_template('register.html')

@app.route('/personal')
def personal():
    if 'username' in session:
        username = session['username']
        ordini_in_corso = users[username]['ordini_in_corso']
        ordini_vecchi = users[username]['ordini_vecchi']
        return render_template('personal.html', username=username, ordini_in_corso=ordini_in_corso, ordini_vecchi=ordini_vecchi)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
