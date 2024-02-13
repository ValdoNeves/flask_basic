# Renderização

o diretório template de estar na raiz do código

podemos usar render_template('index.html)

também podemos usar o url_for e passar o nome da função, mas isso irá retorna apenas o seu decorator por exemplo

~~~
@app.router("/about")
def about():
    ...restante do codigo..
~~~

utilizando url_for(about) em uma função anterior ou posterior a about o retorno será "/about"

mas para utilizar algo dessa forma o que realmente queremos é que o entrar na rota "/" o sistema redireciona para a tela about e para isso utilizamos o "redirect" que também faz parte do flask

~~~
@app.router("/")
def index():
    return redirect(url_for('about))

@app.router("/about")
def about():
    ...restante do codigo..
~~~

agora quando acessado o caminho raiz o navegador será redirecionado para about