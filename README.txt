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
		Por exemplo, podemos criar o seguinte roteamento: @app.route('/menu') ou
			@app.route('/menu/sobre_a_emprese') ... É sempre uma boa prática fazer uma aplicação com
			essas rotas, uma vez que facilita a navegação do usuário.
	* O retorno da nossa função hello_world é o que será consderado como html quando a rota indicada for
		acessada. Exemplo: return "<h1>OI</h1>" ---> a palavra OI, que está dentro da tag html h1, aparecerá
		destacada na página.

- Para rodar a aplicação criada (no prompt de comando do Windows):
        set FLASK_APP=main.py
        python3 -m flask run

- Uma coisa muito útil e interessante sobre o roteamento é que é possível usar VARIÁVEIS NA ROTA! Ou seja, podemos
	ter várias rotas em apenas uma função. Exemplo:
		@app.route('/<variavel>')
		def escreve_variavel_na_tela(variavel):
			return f'A variável é: {variavel}'
	Nesse contexto, também é possível converter a variável para um tipo específico:
		Tipos possíveis:
			* string (é o padrão) ---> aceita qualquer texto que não contenha /
			* int ---> aceita inteiros positivos
			* float ---> aceita floats positivos
			* path ---> o mesmo que string, mas aceita /
			* uuid ---> aceita strings UUID (Identificador Único Universal -> "é um número de 128 bits
				usado para identificar informações em sistemas de computação" fonte: Wikipedia)
		Para especificar o tipo desejado, basta seguir a seguinte notação: <conversor:nome_da_variável>;
		Exemplo:
			@app.route('/<int:senha>)
			def mostrar_senha(senha):
				return f'Sua senha é: {senha}'

- Enquanto ainda passamos o html de uma página diretamente no retorno da função respectiva à página, é interessante
	usarmos a biblioteca markupsafe, que implementa um objeto de texto que analiza os caracteres da string e
	torna seguro apresentá-los na página HTML ou mesmo em arquivos XML. Assim, caracteres com significados 
	especiais são apresentados como strings normais. Usar essa biblioteca pode evitar ataques de injeção.
		Instalação:
			pip3 install MarkupSafe
		Exemplo de uso:
			@app.route('/testando_markupsafe)
			def testando_markupsafe():
				cmd = "<script>alert('oi');</script>"
				return f'{escape(cmd)}'
		Se, no exemplo acima, o método escape não fosse aplicado, o código javascript contido na variável
			cmd seria executado, assim, o método se apresenta como forma de proteção do seu programa
			contra ataques de injeção maliciosos.

- Criando URLs (URL Building) ---> para criar uma URL para uma função específica, existe o método url_for(), que 
	deve ser importado de flask (from flask import Flask, url_for).
	O primeiro argumento do método url_for() se refere ao nome da função a qual se deseja associar a url.
	Os demais argumentos podem ser de dois tipos:
		* Se a variável ao argumento for conhecida e se refira a um argumento da função indicada,
			então é passada à função desejada;
		* Se a variável ao argumento não for conhecida, então são anexadas à URL como parâmetros query.
	Utilizar o método url_for() facilita a criação de URLs.
	Exemplo baseado no da própria documentação do Flask:
		from flask import Flask, url_for
		from markupsafe import escape

		app = Flask(__name__)

		@app.route('/')
		def index():
		    return 'index'

		@app.route('/login')
		def login():
		    return 'login'

		@app.route('/user/<username>')
		def profile(username):
		    return '{}\'s profile'.format(escape(username))

		url_for('index') # cria a seguinte URL: /
		url_for('login') # cria a seguinte URL: /login
		url_for('login', next='/') # cria a seguinte URL: /login?next=/
		url_for('profile', username='John Doe') # cria a seguinte URL: /user/John%20Doe
		
	Contudo, o código apresentado acima não funcionará, uma vez que é necessário declarar um contexto.
	Por enquanto, utilizaremos o método test_request_context() como contexto.
	Exemplo da própria documentação do Flask:
		from flask import Flask, url_for
		from markupsafe import escape
		
		app = Flask(__name__)
		
		@app.route('/')
		def index():
		    return 'index'
		
		@app.route('/login')
		def login():
		    return 'login'
		
		@app.route('/user/<username>')
		def profile(username):
		    return '{}\'s profile'.format(escape(username))
		
		with app.test_request_context():
		    print(url_for('index'))
		    print(url_for('login'))
		    print(url_for('login', next='/'))
		    print(url_for('profile', username='John Doe'))

- 
