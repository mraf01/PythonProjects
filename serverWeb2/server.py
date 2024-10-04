from flask import Flask, render_template, request

app = Flask(__name__)

utenti_registrati = [
    ["Mario", "Rossi", "PASSWORD1234", "M"],
    ["Fabio", "Bianchi", "PASSWORD9876", "M"],
    ["Chiara", "Verdi", "PASSWORD4537", "F"]
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/abc')
def index2():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    password = request.args.get('password')

    if nome and cognome and password:
        for utente in utenti_registrati:
            nome_utente, cognome_utente, password_utente, sesso_utente = utente

            if nome.lower() == nome_utente.lower() and cognome.lower() == cognome_utente.lower() and password == password_utente:
                return render_template('index2.html', nome=nome, cognome=cognome, sesso=sesso_utente)

        error_message = 'Utente non registrato o password errata.'
        return render_template('error.html', error_message=error_message)

    else:
        error_message = 'Registrazione incompleta: Fornisci "nome", "cognome" e "password".'
        return render_template('error.html', error_message=error_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
