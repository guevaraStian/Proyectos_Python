from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'basededatos'
mysql = MySQL(app)

app.secret_key='mysecretkey'



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto')
    data= cur.fetchall()
    print(data)
    return render_template('index.html', contacto = data)

@app.route('/add_contacto', methods=['POST'])
def add_contacto():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        celular = request.form['celular']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacto (id, nombre, celular, email) VALUES (%s,%s,%s,%s)', (id, nombre, celular, email))
        mysql.connection.commit()
        flash('Contacto agregado')
        return redirect(url_for('Index'))


@app.route('/borrar/<string:id>')
def borrar_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacto WHERE id ={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado')
    return redirect(url_for('Index'))

@app.route('/editar/<id>',methods = ['POST', 'GET'])
def get_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editarcontacto.html', contacto= data[0])

@app.route('/update/<id>', methods = ['POST'])
def updatecontact(id):
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        celular = request.form['celular']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE contacto
        SET nombre = %s,
        celular = %s,
        email = %s
        WHERE id = %s
        """,(nombre, celular, email,id))
        mysql.connection.commit()
        flash('Contacto editado')
        return redirect(url_for(Index))

if __name__=='__main__':
    app.run(port=3000, debug=True)