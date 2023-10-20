from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route("/lab2/example")
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
@lab2.route("/lab2/")
def lab ():
    return render_template('lab2.html')
@lab2.route("/lab2/series")
def series ():
    return render_template('series.html')
