from flask import Blueprint, url_for, render_template, request, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route("/lab3/")
def lab ():
    return render_template('lab3.html')


@lab3.route("/lab3/form1")
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route("/lab3/order")
def order ():
    return render_template('order.html')


@lab3.route("/lab3/pay")
def pay ():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price = price)


@lab3.route("/lab3/success")
def success ():
    return render_template('success.html')

@lab3.route("/lab3/form2")
def form2 ():
    return render_template('form2.html')

@lab3.route("/lab3/bilet")
def bilet():
    user = request.args.get('user')
    age = request.args.get('age')
    vyezs = request.args.get('vyezs')
    nazn = request.args.get('nazn')
    polka = request.args.get('polka')
    bag = request.args.get('bag')
    data = request.args.get('data')
    return render_template('bilet.html', user=user, age=age, vyezs=vyezs, nazn=nazn, polka=polka, bag=bag, data=data)

@lab3.route("/lab3/zachita/<int:h1>/<int:h2>/<int:h3>/<int:h4>/")
def zachita (h1, h2, h3, h4):
    vch1 = request.args.get('vch')
    ch1 = request.args.get('ch')
    vch = float(vch1)
    ch = int(ch2)
    summ = vch
    for i in range(1, ch):
        factorial = 1
        for u in range(2*i+2):
            factorial += factorial*u
        summ += ((-1)**i)*(vch**(2*i+1))/factorial


    m = [h1, h2, h3, h4]
    for i in range(4):
        if(i<=2) and (m[i] == m[i+1]):
            k = m[i]
    for i in range(4):
        if m[i] != k:
            g = i
    return render_template('zachita.html', g=g, vch=vch, ch=ch, summ=summ)

