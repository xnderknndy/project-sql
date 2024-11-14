from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "genshin"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""

mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/simpan', methods=["POST", "GET"])
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
    return "Saved"

@app.route('/tampil')
def tampil():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM buildchr")
    data = cursor.fetchall()
    cursor.close()
    return render_template('tampil.html', data=data)

@app.route('/hapus/<int:id>')
def hapus(id):
    cursor = mysql.connection.cursor()
    query = "DELETE FROM buildchr WHERE id = %s"
    cursor.execute(query, (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect('/tampil')

@app.route('/update/<int:id>')
def update(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM buildchr WHERE id = %s"
    cursor.execute(query, (id,))
    value = cursor.fetchone()
    cursor.close()
    return render_template('update.html', value=value)

@app.route('/aksiupdate/<int:id>', methods=["POST", "GET"])
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
