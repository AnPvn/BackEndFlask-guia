Passo a passo para criar seu BackEnd (se necessário, o de front-end virá em breve):

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

- Métodos HTTP ---> Antes de construirmos de fato nosso back-end, é necessário conhecer os métodos HTTP. São eles:
	GET, POST, HEAD, PUT, DELETE, TRACE, OPTIONS, CONNECT, PATCH.
	Por enquanto, apenas utilizaremos os métodos GET e POST. Após esse passo a passo, recomendo se familiarizar
		com os demais métodos.
	GET: Requisita uma representação de um recurso, os tipos de represenação mais comuns são os formatos JSON e
		XML. Esses parâmetros enviados podem ser vistos pela URI.
	POST: Envia os parâmetros no corpo da requisição.
	
	OBS!: O protocolo http não promove segurança, para que os dados enviados sejam realmente protegidos,
		utilize o protocolo https!

	Por padrão, o método route() do Flask apenas responde à métodos GET. Para utilizar outros métodos, 
		é necessário passá-los como argumentos para o route(). Exemplo:
			
			from flask import Flask, request

			app = Flask(__name__)

			@app.route('/página1', methods=['GET, POST'])
			def pagina1():
			    if(request.method == 'POST'):
				return 'alguma coisa'
			    elif(request.method == 'GET'):
				return 'outra coisa'

		Perceba que os métodos HTTP utilizados são passados em forma de lista para o parâmetro methods.
		O exemplo da prórpia página do Flask:
			
			from flask import request

			@app.route('/login', methods=['GET', 'POST'])
			def login():
			    if request.method == 'POST':
			        return do_the_login()
			    else:
			        return show_the_login_form()

- Static Files ---> Uma página apenas com HTMl não faz muita coisa, é realmente interessante utilizar CSS e
	JavaScript para respectivamente implementar beleza e funcionalidade à sua página.
	Seus arquivos js e css e imagens são ditos como Static Files ('arquivos estátivos'), e para usá-los na sua
		aplicação com o Flask, é necessário criar uma pasta no seu projeto chamada static, que conterá todos
		os seus arquivos desse tipo.
			mkdir static
	Mas como invocar um determinado elemento de um determidado arquivo em uma determinada página HTML?
	Entenderemos a seguir...

- Rendering Templates ---> Até agora, passávamos o html para uma rota através do retorno do método referente à rota,
	via strings, como no exemplo:
		@app.route('/rota_exemplo'):
		def rota_exemplo():
			return '<html><head><title>Rota exemplo</head><body><h1>Rota Exemplo</h1></body></html>'

	Embora funcione, temos que concordar que além de feio, dificulta o desenvolvimento do projeto conforme
		o crescimento do mesmo.
	Para solucionar tal problema, há um método no Flask chamado render_template(). Com ele, podemos enviar nosso
		arquivo html para a rota desejada juntamente com as variáveis que desejamos passar para o nosso
		template.
	Exemplo do prórpio flask (adaptado)
		
		from flask import Flask, render_template
		app = Flask(__name__)

		@app.route('/hello/')
		@app.route('/hello/<name>')
		def name(name=None):
		    return render_template('hello.html', name=name)

	Nesse exemplo, podemos perceber duas coisas:
		* Podemos direcionar a mesma função para mais de uma rota;
		* Utilizamos o método render_template() para passar o arquivo hello.html para as duas rotas,
			especificando o parâmetro name como sendo a variável name, que por padrão é None.
	
	Todos os seus templates (seus html) devem estar na pasta templates, portanto, você deve criá-la:
		mkdir templates

	No exemplo anterior, perceba que estamos especificando a variável name, mas como utilizá-la no template?
	O Flask utiliza um mecanismo de modelo da Web denominado Jinja2, e com ele é possível utilizar um pouco de
		'python' dentro de seu html, utilizando o seguinte padrão:
			---> {% palavra-chave %} para comandos como if e else
			---> {{ variável }} para usar o valor da variável.
	Exemplo:
		{% if name %}
			<h1>Seu nome é: {{ name }} </h1>
		{% else %}
			<h1>Não sei seu nome</h1>
		{% endif %}
	
	Dentro de templates, você também tem acesso para os objetos request, session, e g, bem como ao método
		get_flashed_messages(). É recomendável você pesquisar sobre eles após esse passo-a-passo,
		entretando, deixo aqui um pouco do objeto session:
			O objeto session é muito semelhante a um dicionário comum do python, com a única diferença
				de que deixa rastros de suas modificações.
				Atributos interessantes do objeto session:
				* new: True se o session é novo e False se não.
				* modified: Indica se o session já foi modificado ou não, importante destacar que
					deve ser alterado manualmente, pois não se altera automaticamente.
					Funciona como um auxílio durante o desenvolvimento de uma aplicação.
				* permanent: Se modificar o valor desse atributo para True, a session terá um tempo
					de vida padrão de 31 dias, se modificado para False, morrerá assim que o
					usuário desconectar de sua página.
		Outro objeto interessante para armazenar data, é o g, mas não discutiremos sobre ele neste guia.
	
	Para maior segurança utilizando esse recurso do Jinja2, você pode utilizar o módulo Markupsafe, que já
		utilizamos anteriormente neste tutorial, evitando ataques de injeção.

- Acessing Request Data ---> Sempre e fundamental que o servidor reaja às informações que o usuário envia. No Flask,
	essa informação está contida no objeto global request. Para entender como esse objeto se torna global, 
	você pode procurar na documentação do Flask por 'Context Locals', mas como não é o objetivo deste guia, 
	pularemos essa informação e seguiremos para 'Como usar o objeto request'...
	
	* request.method ---> O atributo method informa o método http que a função está trando em determinado
		momento.
	* request.form ---> O atributo form é usado para acessar as informações que estão sendo transmitidas pelo o 
		método que está sendo usado, seja ele POST ou PUT. Ele é um dicionário.
	* request.args ---> O atributo args é usado para acessar os parâmetros passados através da URL (?key=value), 
		(enviados pelo método GET).
	
	Exemplo retirado da documentação do Flask:

		@app.route('/login', methods=['POST', 'GET'])
		def login():
		    error = None
		    if request.method == 'POST':
		        if valid_login(request.form['username'], request.form['password']):
		            return log_the_user_in(request.form['username'])
		        else:
			    error = 'Invalid username/password'
		    return render_template('login.html', error=error)

	É importante informar que a chave especificada quando invoca o atributo form, corresponde ao atributo name
		de uma tag html de formulário. Exemplo:
			<form method="post">
			    <label for="username">Username</label>
			    <input type="text" name="username" id="username">
			    <label for="password">Password</label>
			    <input type="password" name="password" id="password">
			    <input type="submit">
			</form>
	
	Se não existir a chave especificada no atributo form, a exceção KeyError é lançada, e se não for tratada,
		uma página de erro HTTP 400 Bad Request é mostrada.

	Outro atributo comumente usado é o args. Exemplo retirado da documentação do Flask:
		searchword = request.args.get('key', '')

- File Uploads ---> Em diversas aplicações web, o usuário pode enviar arquvios para o servidor. E com o Flask, esse
	processo é bem simples.
	Antes de tudo, no formulário html, é necessário atribuir o seguinte atributo: enctype="multipart/form-data",
		para que o navegador possa transmitir esses arquivos para o servidor.
	Para salvar o arquivo na memória do servidor, existe o método save(). Exemplo da documentação do Flask:
		from flask import request

		@app.route('/upload', methods=['GET', 'POST'])
		def upload_file():
		    if request.method == 'POST':
		        f = request.files['the_file']
		        f.save('/var/www/uploads/uploaded_file.txt')

	Para saber como o arquivo era nomeado pelo usuário antes do upload, existe o atributo filename, embora não
		seja muito confiável, uma vez que pode ser facilmente alterado/forjado. Para ter com segurança o
		nome original do arquivo, é possível utilizar o método secure_filename() da biblioteca Werkzeug.
		Exemplo da documentação do Flask:
			from flask import request
			from werkzeug.utils import secure_filename
			
			@app.route('/upload', methods=['GET', 'POST'])
			def upload_file():
			    if request.method == 'POST':
			        f = request.files['the_file']
			        f.save('/var/www/uploads/' + secure_filename(f.filename))


- Cookies ---> Os Cookies são arquivos usados para armazenar informações sobre os usuários, geralmente auxiliando-os
	a navegar no site. Por exemplo, uma loja virtual pode utilizar os Cookies para armazenar os produtos 
	anteriormente acessados por um determinado usuário e dessa forma, recomendar outros produtos relacionados
	com os anteriores.
	
	Com o Flask, o uso de Cookies é bem simples.

	* cookies ---> O atributo cookies é usado para acessar os cookies. É um dicionário que contém todos os 
		cookies referentes ao usuário. Exemplo da documentação do Flask:
			from flask import request
			
			@app.route('/')
			def index():
			    username = request.cookies.get('username')

		Usar cookies.get(key) no lugar de cookies[key] evita o erro KeyError.

	* set_cookies ---> O atributo set_cookies pe usado para alterar o conteúdo dos cookies. Exemplo da
		documentação do Flask:
			from flask import make_response

			@app.route('/')
			def index():
			    resp = make_response(render_template(...))
			    resp.set_cookie('username', 'the username')
			    return resp

- Redirecionamento e Erros ---> Esse é um tópico em que não há muito segredo, portanto apenas apresentarei os 
	exemplos contidos na página de documentação do Flask.

	* Redirecionamento e abortar uma requisição:
		from flask import abort, redirect, url_for

		@app.route('/')
		def index():
		    return redirect(url_for('login'))
		
		@app.route('/login')
		def login():
		    abort(401)
		    this_is_never_executed()

	* Para customisar uma página de erro, é possível usar o decorator errorhandler():
		from flask import render_template

		@app.errorhandler(404)
		def page_not_found(error):
		    return render_template('page_not_found.html'), 404

- Uma última consideração - Responses ---> Uma boa prática a ser feita quando está se fazendo uma aplicação com o
	Flask, é utilizar o método make_response() antes de retornar o template para a página, pois assim, ainda
	é possível fazer algumas modificações antes de retornar, como no exemplo retirado da documentação do Flask:
		@app.errorhandler(404)
		def not_found(error):
		    resp = make_response(render_template('error.html'), 404)
		    resp.headers['X-Something'] = 'A value'
		    return resp


Essa foi apenas uma pequena introdução ao micro-framework Flask. Como você já deve ter percebido, esse passo-a-passo
	é extremamente baseado na documentação do Flask, com poucos detalhes diferentes e está em português.
	Foi uma maneira que encontrei de revisar o funcionamento do micro-framework e simultâneamente fazer um guia 
	para acompanhar o desenvolvimento de uma aplicação com meu amigo.

É importante dizer que o Flask não se limita a apenas o que foi apresentado aqui, outros tópicos que recomendo
	pesquisar após este passo-a-passo são:

		* Extensões do Flask;
		* Enviar a aplicação para um Servidor Web.
	
	E obviamente, são encontradas na própria documentação do Flask.
