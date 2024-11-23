from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "genshin"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""

mysql = MySQL(app)

def login_required(func):
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__ 
    return wrapper

@app.route('/')
@app.route('/home')
@login_required
def home():
    username = session.get("user")
    return render_template("home.html", username=username)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/aksi_login', methods=["POST", "GET"])
def aksi_login():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM user WHERE username = %s AND password = %s"
    data = (request.form['username'], request.form['password'])
    cursor.execute(query, data)
    value = cursor.fetchone()
    cursor.close()

    if value:
        session["user"] = request.form['username']
        return redirect(url_for("home")) 
    else:
        return "Invalid username or password."

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route('/simpan', methods=["POST", "GET"])
@login_required
def simpan():
    nama = request.form["nama"]
    artifact = request.form["artifact"]
    weapon = request.form["weapon"]
    main_stat = request.form["main_stat"]
    sub_stat = request.form["sub_stat"]
    cursor = mysql.connection.cursor()
    query = "INSERT INTO buildchr (id, nama, artifact, weapon, main_stat, sub_stat) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (None, nama, artifact, weapon, main_stat, sub_stat)
    cursor.execute(query, data)
    mysql.connection.commit()
    cursor.close()
    return "Saved, go to '/tampil' if you wanna see it."

@app.route('/tampil')
@login_required
def tampil():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM buildchr")
    data = cursor.fetchall()
    cursor.close()
    return render_template('tampil.html', data=data)

@app.route('/hapus/<int:id>')
@login_required
def hapus(id):
    cursor = mysql.connection.cursor()
    query = "DELETE FROM buildchr WHERE id = %s"
    cursor.execute(query, (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect('/tampil')

@app.route('/update/<int:id>')
@login_required
def update(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM buildchr WHERE id = %s"
    cursor.execute(query, (id,))
    value = cursor.fetchone()
    cursor.close()
    return render_template('update.html', value=value)

@app.route('/aksiupdate/<int:id>', methods=["POST", "GET"])
@login_required
def aksiupdate(id):
    nama = request.form["nama"]
    artifact = request.form["artifact"]
    weapon = request.form["weapon"]
    main_stat = request.form["main_stat"]
    sub_stat = request.form["sub_stat"]
    cursor = mysql.connection.cursor()
    query = "UPDATE buildchr SET nama = %s, artifact = %s, weapon = %s, main_stat = %s, sub_stat = %s WHERE id = %s"
    data = (nama, artifact, weapon, main_stat, sub_stat, id)
    cursor.execute(query, data)
    mysql.connection.commit()
    cursor.close()
    return redirect('/tampil')

if __name__ == "__main__":
    app.run(debug=True)
