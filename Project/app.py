from flask import Flask
from flask import render_template, redirect,request,Response,session
from flask_mysqldb import MySQL,MySQLdb

app= Flask(__name__,template_folder='template')

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='login'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

#funcion de login

@app.route('/acceso-login', methods= ["GET","POST"])
def login():

    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword':
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']

        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND password = %s',(_correo,_password,))
        account = cur.fetchone()


        if account:
            session['logeado']=True
            session['id'] = account['id']


            return render_template("admin.html")
        else:
            return render_template("index.html")





    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key="contraseñamela"
    app.run(debug=True, host='0.0.0.0',port=5000,threaded=True)