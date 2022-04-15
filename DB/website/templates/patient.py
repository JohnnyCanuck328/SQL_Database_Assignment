from unicodedata import category
from flask import Blueprint, request,render_template, flash, redirect, url_for, request

import mysql.connector
from mysql.connector import Error
import pandas as pd

patient = Blueprint('patient', __name__)

# connection information
hostName = "localhost"
databaseName = "project"
userName = "root"
passwordString = "1qaz@WSX"

#ID testing
patientID = ""
uid = "123456"

def idCheck(id):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    mycursor.execute("SELECT USERID FROM USER_")
    userid = mycursor.fetchall()

    for uerid in userid:
        if id == userid:
            return True
    return False

@patient.route('/patient/login', methods=['GET', 'POST'])
def login():

    id = request.form.get('pID')
    if request.method == "POST":
        if idCheck(id):
                flash('Success', category='success')
                login = True
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

    return render_template("patientAppointment.html")


@patient.route('/patient/record', methods=['GET', 'POST'])
def record():
    data = request.form

    return render_template("patientRecord.html")

@patient.route('/patient/billing', methods=['GET', 'POST'])
def billing():
    data = request.form

    return render_template("patientBilling.html")
