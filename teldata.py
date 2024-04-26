from flask import Flask,redirect,url_for,render_template,jsonify,request
from flaskext.mysql import MySQL
app=Flask(__name__)
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='45298'
app.config['MYSQL_DATABASE_DB']='telanganagov'
mysql=MySQL(app)
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/allinfo',methods=['GET'])
def info():
    cursor=mysql.get_db().cursor()
    cursor.execute('select *from telanganagov')
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
app.run(use_reloader=True)
