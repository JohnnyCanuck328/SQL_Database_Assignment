from unicodedata import category
from flask import Blueprint, request, render_template, flash, redirect, url_for, request
from jinja2 import MemcachedBytecodeCache

import mysql.connector
from mysql.connector import Error
import pandas as pd

patient = Blueprint('patient', __name__)

# connection information
hostName = "localhost"
databaseName = "project"
userName = "root"
passwordString = "1qaz@WSX"

# ID testing
patientID = ""


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
        patientId = tempID
        return True
    return False


def patientAppointment():
    mydb = mysql.connector.connect(
        host=hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor = mydb.cursor()
    myquery = "SELECT * FROM APPOINTMENT WHERE PATIENT = %s"
    try:
        mycursor.execute(myquery, patientID)
        myresult = mycursor.fetchall()
    except Exception as e:
        print(e)
    else:
        if mycursor.rowcount == 0:
            return (("","","","","","","","","",""))
        else:
            return myresult


def patientRecord():
    mydb = mysql.connector.connect(
        host=hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor = mydb.cursor()
    myquery = "SELECT * FROM RECORD WHERE RECORDID IN (SELECT RECORD FROM APPOINTMENT WHERE PATIENT = %s)"
    try:
        mycursor.execute(myquery, patientID)
        myresult = mycursor.fetchall()
    except Exception as e:
        print(e)
    else:
        if mycursor.rowcount == 0:
            return (("","","","",""))
        else:
            return myresult


def patientBilling():
    mydb = mysql.connector.connect(
        host=hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor = mydb.cursor()
    myquery = "SELECT * FROM PATIENT_BILLING WHERE PROCEDURE_ IN (SELECT PROCEDURE_ID FROM APPOINTMENT_PROCEDURE WHERE PATIENT_PROC = %s))"
    try:
        mycursor.execute(myquery, patientID)
        myresult = mycursor.fetchall()
    except Exception as e:
        print(e)
    else:
        if mycursor.rowcount == 0:
            return (("","","","","","","","",""))
        else:
            return myresult


@patient.route('/patient/login', methods=['GET', 'POST'])
def login():

    id = request.form.get('pID')
    if request.method == "POST":
        if idCheck(id):
            flash('Success', category='success')
            return redirect(url_for('patient.selection'))
        else:
            flash('Invalid patient ID, try again.', category='error')

    return render_template("patientLogin.html")


@patient.route('/patient/selection', methods=['GET', 'POST'])
def selection():
    return '''
        <h2>Hello, Please Choose What You Would Like to Do</h2>

        <button type="button" onclick="location.href='/patient/appointment'">Appointment Information</button>
        <button type="button" onclick="location.href='/patient/record'">Record Information</button><br>

        <button type="button" onclick="location.href='/patient/billing'">Billing Information</button>
        <button type="button" onclick="location.href='/'">Home</button>

    </form>

</body>
</html>
    '''


@patient.route('/patient/appointment', methods=['GET', 'POST'])
def appointment():
    data = request.form

    return render_template("patientAppointment.html", data=patientAppointment())


@patient.route('/patient/record', methods=['GET', 'POST'])
def record():
    data = request.form

    return render_template("patientRecord.html", data=patientRecord())


@patient.route('/patient/billing', methods=['GET', 'POST'])
def billing():
    data = request.form

    return render_template("patientBilling.html", data=patientBilling())
