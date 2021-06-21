from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import MySQLdb
import unittest
from customers import customers
from payments import payments
from maintenance import maintenance
import pdfkit
import hashlib




app = Flask(__name__)
app.register_blueprint(customers)
app.register_blueprint(payments)
app.register_blueprint(maintenance)




#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'halofit'
mysql = MySQL(app)
 # settings
app.secret_key = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'




@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)




@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
        
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        if username and password:
            password = password.encode('utf-8')
            print(password)
            try:
                cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute('SELECT * FROM users WHERE user = %s AND pass = %s', (username, password,))
                account = cur.fetchone()
                cur.close()
                print(account)
            except MySQLdb.Error as e:
                print(e)
                flash('Error')
                return render_template('no_conexion.html', error=e)
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['user']
                # Redirect to home page
                return redirect(url_for('customers.list_customers'))
            else:
                # Account doesnt exist or username/password incorrect
                return render_template('no_conexion.html', error="Usuario o contraseña incorrectos")
            
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))
     
    
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 7070, debug = True)