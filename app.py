from flask import Flask, render_template
from datetime import datetime 


app = Flask (__name__)

print (__name__)

@app.route('/')
def inicio():
    return '<h1>Oii </h1>' 



@app.route ('/sobre')
def sobre():
    return '''
<h1 style='color:red'> Meu nome é: </h1>
<p> Manuela Mariano <b>Pereira</b>
<! -- Tudo que eu pensar em html pode vir aqui -->
'''


@app.route ('/curso')
def curso():
    return '''
<h1 style='color:red'> Cursando </h1>
<p> Gestão de <b>T.I</b>
<! -- Tudo que eu pensar em html pode vir aqui -->
'''


@app.route ('/var')
def variavel():
    palavra = 'Manuela'
    return f'<h1>Adicionando texto de var: {palavra} <h1>'


@app.route('/idade/<int:ano>')
def idade(ano):
    calculoIdade = 2026 - ano
    return f'Você tem {calculoIdade} anos!'


@app.route('/salvar/<nome>/produtos')
def salvar (nome):
    return f'Você salvou o produto [ {nome} ] com sucesso!'


@app.route ('/html')
def pagina_html():
    return render_template('index.html')


@app.route ('/trabalho')
def trabalho():
    palavra = 'Trabalhos'
    return f'<h1>Adicionando texto de var: {palavra} <h1>'


@app.route('/calcular/<nome>/int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status= 'Maior de Idade'

    #--- Fazer para quem tem igual 18 anos ---
    
    else:
        status = 'Menor de Idade - Acesso Negado'

    return render_template ('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status =  status)










# --- ULTIMA COISA DO ARQUIVO ---


if __name__ == '__main__':
    app.run(debug=True)
