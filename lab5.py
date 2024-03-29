from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, Blueprint
from flask import Flask, session
import psycopg2
import datetime
lab5 = Blueprint("lab5", __name__)

def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="kramar_knowledge_base",
        password="000")

    return conn; 

def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@lab5.route("/lab5")
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)
    
    return "go to console" 

@lab5.route("/lab5/glavn") 
def glavn (): 
    visibleUser = "Anon" 
 
    if 'username' in session: 
        visibleUser = session['username'] 

 
    return render_template('glavn.html', username=visibleUser)


@lab5.route("/lab5/users") 
def users (): 
    # Прописываем параметры подключения к БД 
    conn = dbConnect() 
    cur = conn.cursor() 
 
    cur.execute("SELECT * FROM users;") 
 
    result = cur.fetchall() 
 
    names = [row[1] for row in result] 
 
    dbClose(cur, conn) 
 
    return render_template('users.html', names = names)

@lab5.route("/lab5/register", methods=["GET", "POST"])
def registerPage():
    errors = {}

    visibleUser = "Anon"

    if 'username' in session:
        visibleUser = session['username']

    if request.method == "GET":
        return render_template("register.html", username=visibleUser)

    username = request.form.get("username")
    password = request.form.get("password")

    if username == '' or password == '':
        errors = "Заполните поля"
        return render_template("register.html", errors=errors, username=visibleUser)

    hashPassword = generate_password_hash(password)
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s;", (username,
    ))

    if cur.fetchone() is not None:
        errors = "Пользователь уже существут"
        dbClose(cur, conn)
        return render_template("register.html", errors=errors, username=visibleUser)

    cur.execute(f"INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login")

@lab5.route("/lab5/login", methods=["GET", "POST"])
def loginPage():
    errors = []

    visibleUser = "Anon"

    if 'username' in session:
        visibleUser = session['username']

    if request.method == "GET":
        return render_template("login2.html", username=visibleUser)

    username = request.form.get("username")
    password = request.form.get("password")

    if username == '' or password == '':
        errors = "Заполните поля"
        return render_template("login2.html", errors=errors, username=visibleUser)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    result = cur.fetchone()

    if result is None:
        errors = "Неправильный логин или пароль"
        dbClose(cur, conn)
        return render_template("login2.html", errors=errors, username=visibleUser)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur,conn)
        return redirect("/lab5/glavn")
    else:
        errors = "Неправильный логин или пароль"
        return render_template("login2.html", errors=errors, username=visibleUser)

@lab5.route("/lab5/new_articles", methods=["GET", "POST"])
def createArticles():
    errors = []
    userID = session.get("id")
    visibleUser = "Anon"

    if 'username' in session:
        visibleUser = session['username']

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html", username=visibleUser)

        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(text_article) == 0:
                errors = "Заполните текст"
                return render_template("new_article.html", errors=errors, username=visibleUser)

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles(user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id;",
            (userID, title, text_article))

            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_article_id}")

    return redirect("/lab5/login")

@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):

    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
    
        text = articleBody[1].splitlines()

        return render_template("articleN.html", article_text=text, article_title=articleBody[0], username=session.get("username"))

@lab5.route("/lab5/user_articles")
def user_articles():

    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT id, title, is_public FROM articles WHERE user_id = %s", (userID,))

        result = cur.fetchone()

        dbClose(cur, conn)

        return render_template("user_articles.html", result=result, username=session.get("username"))
    return redirect("/lab5/login")  

       