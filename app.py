from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

mydatabase = mysql.connector.connect(user='machoBeaver9@server248514724', password='7718e510-c19a-45ce-b1d5-0015d7ffe82f', host='server248514724.mysql.database.azure.com', port=3306, database='sampledb')

mycursor = mydatabase.cursor()

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/search/<keyword>')
def search(keyword):
    info = (keyword,)
    qltest = """SELECT * FROM job WHERE MATCH(title,details) AGAINST(%s)"""
    mycursor.execute(qltest, info)
    myresult = mycursor.fetchall()
    return render_template('results.html', result = myresult)