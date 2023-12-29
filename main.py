import os
import socket
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'ede1fff6cc8a'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'root' # Password Here
app.config['MYSQL_DB'] = 'flaskdb' # Database Name 
app.config['MYSQL_UNIX_SOCKET'] = '/var/run/mysqld/mysqld.sock'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

hname= socket.gethostname()

@app.route('/')
def home():
    #print(hname)
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT username,hostname,id FROM users''')
    users = cursor.fetchall()
    print(cursor.fetchall())
    # users = curl.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('index.html',hostname=hname,users=users)

@app.route('/add',methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO users(username,hostname) VALUES(%s,%s)''', (json_result['firstName'],hname))
        mysql.connection.commit()
        cursor.close()
        print(json_result)
        return redirect('/')
    return render_template("add.html",hostname=hname)

@app.route('/delete/<int:id>')
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM users WHERE id=%s''', (id,))
    mysql.connection.commit()
    cursor.close()
    print('deleted id: ',id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')