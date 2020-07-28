from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/<variavel>')
def show_variavel(variavel):
    return f'A variável eh: {variavel}'

@app.route('/usuario/<int:senha>')
def show_senha(senha):
    return f'A sua senha é: {senha}'

from markupsafe import escape

@app.route('/testando_markupsafe')
def testando_markupsafe():
    cmd = "<script>alert('oi')</script>"
    return f'Testando o método escape do markupsafe {escape(cmd)}'
    # se o comando escape não fosse utilizado, o código javascript seria executado

@app.route('/testando_espacos/<texto>')
def teste_espacos(texto):
    return "teste espacos {}".format(texto)
