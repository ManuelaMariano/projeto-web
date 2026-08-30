from flask import Flask

app = Flask (__name__)

@app.route('/')
def pagina_inicial():
        return '<h1>Olá</h1>'

@app.route('/nome')
def nome():
        return '<p>Manuela</p>'

if __name__ == '__main':
        app.run(debug=True)
        