from flask import Blueprint, request,render_template, flash, redirect, url_for, request

import mysql.connector
from mysql.connector import Error
import pandas as pd

dentist = Blueprint('dentist', __name__)

# connection information
hostName = "localhost"
databaseName = "project"
userName = "root"
passwordString = "1qaz@WSX"


def idCheck(id):
    mydb = mysql.connector.connect(
        host=hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )

    tempID = (id,)
    mycursor = mydb.cursor()
    myquery = "SELECT USERID FROM USER_ WHERE USERID = %s"

    try:
        mycursor.execute(myquery, tempID)
        myrow = mycursor.fetchall()
        print(myrow)
    except Exception as e:
        print(e)
    else:
        idCount = mycursor.rowcount
        print(idCount)

    if idCount > 0:
        global dentistID
        dentistID = tempID
        return True
    return False


def dentistAppointment():
    mydb = mysql.connector.connect(
        host=hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor = mydb.cursor()
    myquery = "SELECT * FROM APPOINTMENT WHERE DENTIST = %s"
    try:
        mycursor.execute(myquery, dentistID)
        myresult = mycursor.fetchall()
        print(myresult)
    except Exception as e:
        print(e)
    else:
        if mycursor.rowcount == 0:
            return (("null","null","null","null","null","null","null","null","null","null","null"),)
        else:
            return myresult

def dentistProcedure():
    mydb = mysql.connector.connect(
        host=hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor = mydb.cursor()
    myquery = "SELECT * FROM APPOINTMENT_PROCEDURE WHERE APPOINTMENT_ IN (SELECT APPOINTMENT_ID FROM APPOINTMENT WHERE DENTIST = %s)"
    try:
        mycursor.execute(myquery, dentistID)
        myresult = mycursor.fetchall()
        print(myresult)
    except Exception as e:
        print(e)
    else:
        if mycursor.rowcount == 0:
            return (("null","null","null","null","null","null","null","null","null","null"),)
        else:
            return myresult

def dentistTreatment():
    mydb = mysql.connector.connect(
        host=hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor = mydb.cursor()
    myquery = "SELECT * FROM TREATMENT WHERE APPOINTMENT_ IN (SELECT APPOINTMENT_ID FROM APPOINTMENT WHERE DENTIST = %s)"
    try:
        mycursor.execute(myquery, dentistID)
        myresult = mycursor.fetchall()
        print(myresult)
    except Exception as e:
        print(e)
    else:
        if mycursor.rowcount == 0:
            return (("null","null","null","null","null","null","null"),)
        else:
            return myresult

def dentistRecord():
    mydb = mysql.connector.connect(
        host=hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor = mydb.cursor()
    myquery = "SELECT * FROM RECORD WHERE RECORD_ID IN (SELECT RECORD_ FROM APPOINTMENT WHERE DENTIST = %s)"
    try:
        mycursor.execute(myquery, dentistID)
        myresult = mycursor.fetchall()
        print(myresult)
    except Exception as e:
        print(e)
    else:
        if mycursor.rowcount == 0:
            return (("null","null","null","null","null"),)
        else:
            return myresult


@dentist.route('/dentist/login', methods=['GET', 'POST'])
def login():

    id = request.form.get('pID')
    if request.method == "POST":
        if idCheck(id):
            return redirect(url_for('dentist.selection'))
        else:
            flash('Invalid dentist ID, try again.', category='error')

    return render_template("dentistLogin.html")


@dentist.route('/dentist/selection', methods=['GET', 'POST'])
def selection():
    return render_template("dentistSelection.html")


@dentist.route('/dentist/appointment', methods=['GET', 'POST'])
def appointment():
    data = request.form

    return render_template("dentistAppointment.html", data=dentistAppointment())


@dentist.route('/dentist/treatment', methods=['GET', 'POST'])
def treatment():
    data = request.form

    return render_template("dentistTreatment.html", data=dentistTreatment())


@dentist.route('/dentist/procedure', methods=['GET', 'POST'])
def procedure():
    data = request.form

    return render_template("dentistProcedure.html", data=dentistProcedure())


@dentist.route('/dentist/record', methods=['GET', 'POST'])
def record():
    data = request.form

    return render_template("dentistRecord.html", data=dentistRecord())
