Passo a passo para criar seu BackEnd:

- Primeiro de tudo, é necessário criar um Ambiente Virtual, para que não ocorram conflitos entre as versões do
	python conforme seu projeto avança e outros projetos são formados.
	Para criar um Ambiente Virtual usando python3 no Windows:
		mkdir myproject
		cd myproject
		py -3 -m venv venv
	Entretanto, não basta apenas criar o Ambiente Virtual, é necessário também ativa-lo:
		venv\Scripts\activate

- Agora que o Ambiente Virtual já está instalado e ativado, iremos instalar o micro-Framework Flask, que é
	responsável por justamente formar o nosso servidor:
		pip install Flask
	É importante destacar que esse comando instala a última versão do Flask, o que muitas vezes não é o mais 
	recomendado, entretanto, vamos continuar com essa mesmo.

- Agora que já instalamos o Flask e suas dependencias, vamos criar nossa primeira aplicação com o Flask.
	Crie um arquvio .py, como por exemplo: "main.py" ou "index.py" e abra-o no seu editor favorito,
	esse tutorial, utilizarei o editor nano:
		nano main.py
        !!! Atenção !!! ---> NÃO nomear o arquivo como flask.py, pois pode causar conflitos.
	Agora vamos começar a programar nosso servidor:
		from flask import Flask
		app = Flask(__name__)
		@app.route('/')
		def hello_world():
			return 'Hello World'
	Agora uma explicação de cada linha do código:
	* from flask import Flask ---> nesta linha, estamos importando a classe Flask da biblioteca flask, a qual
		instalamos há pouco.
	* app = Flask(__name__) ---> nesta linha, estamos instanciando um objeto Flask na referência app. O
		parâmetro __name__ deve ser usado quando sua aplicação possuir apenas um módulo, isso é necessário 
		uma vez que o Flask utiliza esse parâmetro para encontrar os arquivos que irão compor sua aplicação.
	* @app.route('/') ---> com esta linha, estamos associando uma rota URL a nossa função hello_world, que
		aparece logo abaixo.
	* O retorno da nossa função hello_world é o que será consderado como html quando a rota indicada for
		acessada.

- Para rodar a aplicação criada (no prompt de comando do Windows):
        set FLASK_APP=main.py
        python3 -m flask run



