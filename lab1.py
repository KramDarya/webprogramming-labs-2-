from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start ():
    return redirect("/menu", code=302)


@lab1.route("/menu")
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
            <li><a href="/lab2/" target="_blank">
                Лабораторная работа 2</a></li>   
        </ol>
    </main>
        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Крамар Дарья, Проворова Елена, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1")
def lab ():
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


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
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


@lab1.route("/lab2/example")
def example ():
    name, nomerl, gruppa, nomerk = 'Крамар Дарья, Проворова Елена', '2', '11', '3'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    books = [
        {'avtor': 'Виктория Авеярд', 'name': 'Разрушенный трон', 'genre': 'Фэнтези', 'str': 220},
        {'avtor': 'Рагнар Йонассон', 'name': 'Затмение', 'genre': 'Детектив', 'str': 240},
        {'avtor': 'Роберт Сперанский', 'name': 'Главный критерий', 'genre': 'Психология', 'str': 330},
        {'avtor': 'Хелена Побяржина', 'name': 'Валсарб', 'genre': 'Проза', 'str': 150},
        {'avtor': 'Рагим Джафаров', 'name': 'Саго', 'genre': 'Триллер', 'str': 410},
        {'avtor': 'Дмитрий Строгов', 'name': 'Тысячелетие обмана', 'genre': 'История', 'str': 287},
        {'avtor': 'Николай Бель', 'name': 'росчерк на колене', 'genre': 'Научная литература', 'str': 356},
        {'avtor': 'Артем Вожаков', 'name': 'Интеллектуальные информационные системы', 'genre': 'Бизнес-литература', 'str': 240},
        {'avtor': 'Александр Низаев', 'name': 'Космический наемник', 'genre': 'Фантастика', 'str': 260},
        {'avtor': 'Кейт Хаск', 'name': 'Дикость', 'genre': 'Роман', 'str': 210},
    ]
    return render_template('example.html',
                            name=name, nomerl=nomerl, gruppa=gruppa,
                            nomerk=nomerk, fruits=fruits, books=books)


@lab1.route("/lab2/")
def lab2 ():
    return render_template('lab2.html')


@lab1.route("/lab2/series")
def series ():
    return render_template('series.html')