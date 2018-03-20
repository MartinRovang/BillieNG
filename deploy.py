from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sqlite3 as sql
from tabledefstats import *
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField ,validators
from wtforms.validators import DataRequired

import time, threading
from datetime import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
engine = create_engine('sqlite:///tutorial.db', echo=True)






app = Flask(__name__)
SQLALCHEMY_DATABASE_URI ='sqlite:///tutorial.db'

app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


Playersstats = []
Playersname = []
Playersnumb = []

#Ticks
def tick():
    i = 0
    print("Money given")
    while i < len(Playersstats):
        User.apply_money(Playersstats[i])
        i+=1


def foo():
    tick()
    threading.Timer(60, foo).start()




def insertUser(username,password):
    con = sql.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()




class Players:
    number_of_user = 0
    def __init__(self,health,armor,dmg,money,id):
        Players.number_of_user += 1
        self.health = health
        self.armor = armor
        self.dmg = dmg
        self.money = money
        self.id = id
    def apply_money(self):
        self.money = int(self.money + 1000)

@app.route('/', methods=('GET', 'POST'))
def home():
    if not session.get('logged_in'):
        return render_template('login.html',number_of_user = Players.number_of_user)
    else:
        return render_template('Scoreboard.html',number_of_user = Players.number_of_user, Playersstats = Playersstats,Playersname=Playersname,Playersnumb=Playersnumb,zip=zip)


@app.route('/login', methods=('GET', 'POST'))
def do_admin_login():
    print("test1")
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/register', methods=('GET', 'POST'))
def do_admin_register():
    Username =  str(request.form['uname'])
    Password =  str(request.form['psw'])
    Passwordrep =  str(request.form['psw-repeat'])
    print(Username)
    if Passwordrep != Password:
        flash('password does not match!')
        return render_template('login.html',number_of_user = Players.number_of_user)
    insertUser(Username,Password)
    Playersname.append(Username)
    Playersstats.append(Players(100,10,20,10000,Players.number_of_user))
    Playersnumb.append(Players.number_of_user-1)
    if Players.number_of_user < 2:
        foo()
    return render_template('login.html',number_of_user = Players.number_of_user)



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()




if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run()
