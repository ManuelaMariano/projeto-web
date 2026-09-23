from flask import Flask, render_template, request, redirect, url_for
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


@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade >= 18:
        status = 'Maior de Idade'
    else:
        status = 'Menor de Idade - Acesso Negado'

    return render_template(
        'variaveis.html',
        nome_usuario = nome,
        ano_atual = ano_atual,
        nascimento = ano,
        idade = idade,
        status = status )




@app.route('/dicio')
def dicionario():
    dados = {
        'chave' : 'valor',   
        'curso' : 'GTI',
        'local' : 'Fatec Jahu',
        'semestre' : 4,
    }

    return render_template ('dicio.html', **dados)


@app.route('/condicao/<int:numero>')
def condicao(numero): 
    return render_template ('condicao.html', numero = numero)


@app.route('/formulario', methods=['GET', 'POST'])
def formulario():

    if request.method == "POST":
        nome = request.form.get('nome','Nada enviado')
        num1 = int(request.form['numero1'])
        num2 = float(request.form['numero2'])

        soma = num1 + num2
        sub = num1 - num2
        mult = num1 * num2
        div = num1 / num2

        return redirect(url_for('exibir_resultado',nome=nome,soma=soma,sub=sub,mult=mult,div=div))

    return render_template('formulario.html')


@app.route('/exibir')
def exibir_resultado():
    nome = request.args.get('nome')
    soma = request.args.get('soma')
    sub = request.args.get('sub')
    mult = request.args.get('mult')
    div = request.args.get('div')

    return render_template(
        'exibir.html',nome=nome,soma=soma,sub=sub,mult=mult,div=div)






# --- ULTIMA COISA DO ARQUIVO ---


if __name__ == '__main__':
    app.run(debug=True)
