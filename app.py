from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start ():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu ():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            «НГТУ,ФБ, WEB-программирование, часть 2. Список лабораторных»
        </header>
        <main>
        <h1>Лабораторные работы по WEB-программированию</h1>
        <ol>
            <li><a href="/lab1" target="_blank">
                Лабораторная работа 1</a></li>   
        </ol>
    </main>
        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Крамар Дарья, Проворова Елена, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1 ():
    return """
<!doctype html>
<html>
    <head>
        <title>Крамар Дарья, Проворова Елена, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная 1
        </header>

        <h1>web-сервер на flask</h1>
        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div>
        <ol>
            <li><a href="/menu" target="_blank">
                Лабораторная работа 1</a></li>   
        </ol>

        <footer>
            &copy; Крамар Дарья, Проворова Елена, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak ():
    return '''
<!doctype html>
<html>
    <body>
        <h1 class="qw">Дуб<!h1>
        <p class="ty">
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </p>
    </body>
</html>
'''
@app.route('/lab1/student')
def nstu ():
    return '''
<!doctype html>
<html>
    <body>
        <h1 class="po">Крамар дарья Николаевна<!h1>
        <p class="tp">
        <img src="''' + url_for('static', filename='nstu.png') + '''">
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </p>
    </body>
</html>
'''

@app.route("/lab2/example")
def example ():
    name, nomerl, gruppa, nomerk = 'Крамар Дарья, Проворова Елена', 'Лабораторная работа 2', '11', '3'
    return render_template('example.html')
