from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route("/lab4/")
def lab ():
    return render_template('lab4.html')

@lab4.route("/lab4/login", methods = ['GET', 'POST'])
def login ():
    if request.method == 'GET':
        return render_template('login.html')
    errors = {}
    username = request.args.get('username')
    password = request.args.get('password')
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('sucess.html')
   
    err = 'Неверные логин и/или пароль'
    return render_template('login.html', username=username, password=password, err=err, errors=errors)

@lab4.route("/lab4/holod", methods = ['GET', 'POST'])
def holod ():
    if request.method == 'GET':
        return render_template('holod.html')
    error = {}
    result = {}
    result2 = {}
    temp = request.form.get('temp')
    if temp == '':
        error = 'Ошибка: не задана температура'
        result = ''
        result2 = ''
    elif int(temp) < -12:
        result = 'Слишком низкое значение'
    elif int(temp) < -1:
        result = 'Слишком высокое значение'
    elif -12 <= int(temp) <= -9:
        result =f'Установлена температура: {temp} C'
        result2 = '❄❄❄'
    elif -8 <= int(temp) <= -5:
        result =f'Установлена температура: {temp} C'
        result2 = '❄❄'
    else:
        result =f'Установлена температура: {temp} C'
        result2 = '❄'
    return render_template('holod.html', temp=temp, error=error, result=result, resuil2=result2)

@lab4.route("/lab4/zerno", methods = ['GET', 'POST'])
def zerno ():
    if request.method == 'GET':
        return render_template('zerno.html')
    error = {}
    result = {}
    price = {}
    zerno = request.form.get('zerno')
    ves = request.form.get('ves')
    if zerno == 'ячмень':
        price = 12000
    elif zerno == 'овес':
        price = 8500
    elif zerno == 'пшеница':
        price = 8700
    else:
        price = 14000
    if ves == '':
        error = 'Не веден вес'
    elif int(ves) <= 0:
        error = 'Неверное значение веса'
    elif 50 <= int(ves) < 500:
        price = price * int(ves) * 0.9
        result = f'Сумма к оплате с учетом скидки 10%: {price}'
    elif int(ves) >= 500:
        error = 'Такого объема нет в наличие, укажите меньший объем'
    else:
        price = price * int(ves)
        result =f'Сумма к оплате: {price}'
    return render_template('zerno.html', zerno=zerno, ves=ves, error=error, result=result)
    

