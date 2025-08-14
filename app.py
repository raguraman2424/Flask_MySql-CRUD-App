from weakref import ref
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Ragu@Muthu5"
app.config["MYSQL_DB"] = "project"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Home Page Route
@app.route("/")
def home():
    cur = mysql.connection.cursor()
    sql = "SELECT * FROM users"
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    return render_template("home.html", datas=res)

# Add User Route
@app.route("/addUser", methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        age = request.form.get('age')

        cur = mysql.connection.cursor()
        sql = "INSERT INTO users (name, city, age) VALUES (%s, %s, %s)"
        cur.execute(sql, (name, city, age))
        mysql.connection.commit()
        cur.close()
        flash('User Details Added')
        return redirect(url_for("home"))
    return render_template("addUsers.html")

# Update User Route
@app.route("/editUser/<string:id>", methods=['GET', 'POST'])
def editUser(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        age = request.form.get('age')
        sql = "UPDATE users SET NAME=%s, CITY=%s, AGE=%s WHERE ID=%s"
        cur.execute(sql, (name, city, age, id))
        mysql.connection.commit()
        cur.close()
        flash('User Details Updated')
        return redirect(url_for("home"))

    # GET method: fetch user info
    sql = "SELECT * FROM users WHERE ID=%s"
    cur.execute(sql, [id])
    res = cur.fetchone()
    cur.close()
    return render_template("editUser.html", datas=res)

# Delete User Route
@app.route('/deleteUser/<string:id>', methods=['GET'])
def deleteUser(id):
    cur = mysql.connection.cursor()
    sql = "DELETE FROM users WHERE ID=%s"
    cur.execute(sql, [id])
    mysql.connection.commit()
    cur.close()
    flash('User Details Deleted')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.secret_key = "6385"
    app.run(debug=True,port=5001)
