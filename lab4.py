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

