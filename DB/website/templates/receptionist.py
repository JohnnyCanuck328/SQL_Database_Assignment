from flask import Blueprint, request, flash, redirect, url_for, request
#import js2py
 
import mysql.connector
from mysql.connector import Error
import pandas as pd
 
receptionist = Blueprint('receptionist', __name__)
 
 
##connection information
hostName = "localhost"
databaseName = "project"
userName = "root"
passwordString = "1qaz@WSX"
 
 
#Interface methods-----------------------------------------------------------------------------
 
 
###HANDLES PATIENT-----------------------------------------------------------
def patientInsertion(pID, gID, gender, DoB, insurance, email, status):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO patient (patient_id, gender, insurance, email_address, date_of_birth, age_status, guardian_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (pID, gender, insurance, email, DoB, status, gID)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def patientUpdate(pID, gender, insurance, email, DoB, status, gID):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update patient set gender = %s, insurance = %s, email_address = %s, date_of_birth = %s,
     age_status = %s, guardian_id = %s where PATIENT_ID = %s"""
    data = (gender, insurance, email, DoB, status, gID, pID)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")
 
 
 
 
 
###HANDLES PATIENTPHONE-----------------------------------------------------------
def phoneInsertion(pID, phone):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO patient_phone (patient_, phone_number) VALUES (%s, %s)"
    data = (pID, phone)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def phoneUpdate(pID, phone):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update patient_phone set patient_ = %s where PATIENT_ID = %s"""
    data = (pID, phone)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")
 
 
 
###HANDLES EMPLOYEE-----------------------------------------------------------
def employeeInsertion(id, role, salary, branch):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO employee (employee_id, role_, salary, branch_id) VALUES (%s, %s, %s, %s)"
    data = (id, role, salary, branch)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def employeeUpdate(id, role, salary, branch):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update employee set role_ = %s, salary = %s, branch_id = %s where employee_id = %s"""
    data = (role, salary, branch, id)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")
 
 
###HANDLES EMPLOYEE LOCATION-----------------------------------------------------------
def locationInsertion(branch, id):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO employee_location (branch_id, employee_id) VALUES (%s, %s)"
    data = (branch, id)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
 
 
###HANDLES APPOINTMENT-----------------------------------------------------------
def appointmentInsertion(id, start, end, date, appointmenttype, status, room, patient, dentist, record, invoice):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    mySql_insert_query = """INSERT INTO appointment (appointment_id, start_time, end_time, date_, appointment_type, staus,
    room_assigned, patient, dentist, record_, invoice_) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    data = (id, start, end, date, appointmenttype, status, room, patient, dentist, record, invoice)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def appointmentUpdate(id, start, end, date, appointmenttype, status, room, patient, dentist, record, invoice):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update appointment set start_time = %s, end_time = %s, date_ = %s, appointment_type = %s, staus = %s, room_assigned = %s,
    patient = %s, dentist = %s, record_ = %s, invoice_ = %s where appointment_id = %s"""
    data = (start, end, date, appointmenttype, status, room, patient, dentist, record, invoice, id)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")
 
 
###HANDLES BRANCH-----------------------------------------------------------
def branchInsertion(id, city, manager, recep1, recep2):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO branches (branch_id, city, manager, receptionist1, receptionist2) VALUES (%s, %s, %s, %s, %s)"
    data = (id, city, manager, recep1, recep2)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def branchUpdate(id, city, manager, recep1, recep2):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update branches set city = %s, manager = %s, receptionist1 = %s, receptionist2 = %s where branch_id = %s"""
    data = (city, manager, recep1, recep2, id)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")
 
 
###HANDLES PROCEDURE-----------------------------------------------------------
def procedureInsertion(id, code, date, patient, toothInvolved, type, appointment, desc, dose, invoice):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO appointment_procedure (procedure_id, procedure_code, date_, patient_proc, tooth_involved, proc_type, appointment_, description, dose_amount, invoice_) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, s)"
    data = (id, code, date, patient, toothInvolved, type, appointment, desc, dose, invoice)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def procedureUpdate(id, code, date, patient, toothInvolved, type, appointment, desc, dose, invoice):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update appointment_procedure set procedure_code = %s, date_ = %s, patient_proc = %s, tooth_involved = %s, proc_type = %s, appointment = %s,
    description = %s, dose_amount = %s, invoice_ = %s where id = %s"""
    data = (code, date, patient, toothInvolved, type, appointment, desc, dose, invoice, id)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")
 
 
###HANDLES INVOICE-----------------------------------------------------------
def invoiceInsertion(iID, pID, DoI, contact, pCharge, iCharge, penalty):
    mydb = mysql.connector.connect(
        host=hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor = mydb.cursor()
    mySql_insert_query = "INSERT INTO invoice (invoice_id, date_of_issue, contact_information, patient_charge, insurance_charge, total_fee_charge, discount, penalty) VALUES (%s, %s, %s, %s, %s, %s,%s, %s)"
    checkIfEmployeeQuery = 'SELECT * FROM EMPLOYEE WHERE EMPLOYEE_ID = {}'.format(pID)

    mycursor.execute(checkIfEmployeeQuery)
    isEmployee = mycursor.fetchall()
    if len(isEmployee) == 0:
        discount = 0
    else:
        discount = 0.5
    pCharge = float(pCharge) - float(pCharge) * discount
    totalFee = pCharge + float(iCharge)

    data = (iID, DoI, contact, pCharge, iCharge, totalFee, discount, penalty)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")


def invoiceUpdate(iID, pID, DoI, contact, pCharge, iCharge, penalty):
    mydb = mysql.connector.connect(
        host=hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor = mydb.cursor()
    sql_update_query = """Update invoice set date_of_issue = %s, contact_information = %s, patient_charge = %s, insurance_charge = %s, total_fee_charge = %s, discount = %s,
    penalty = %s where invoice_id = %s"""
    checkIfEmployeeQuery = 'SELECT * FROM EMPLOYEE WHERE EMPLOYEE_ID = {}'.format(pID)

    mycursor.execute(checkIfEmployeeQuery)
    isEmployee = mycursor.fetchall()
    if len(isEmployee) == 0:
        discount = 0
    else:
        discount = 0.5
    pCharge = float(pCharge) - float(pCharge) * discount
    totalFee = pCharge + float(iCharge)

    data = (DoI, contact, pCharge, iCharge, totalFee, discount, penalty, iID)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")


###HANDLES FEE-----------------------------------------------------------
def feeInsertion(feeID, procedure, code, charge):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO fee_charge (fee_identifier, procedure_, fee_code, charge) VALUES (%s, %s, %s, %s)"
    data = (feeID, procedure, code, charge)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def feeUpdate(feeID, procedure, code, charge):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update fee_charge set procedure_ = %s, fee_code = %s, charge = %s where fee_identifier = %s"""
    data = (procedure, code, charge, feeID)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")
 
 
###HANDLES BILLING-----------------------------------------------------------
def billingInsertion(id, date, start, end, proc, pBilling, iBilling, tBill, payment):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO patient_billing (billing_id, date_of_visit, start_time, end_time, procedure_, patient_portion, insurance_portion, total_billing, pay) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (id, date, start, end, proc, pBilling, iBilling, tBill, payment)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def billingUpdate(id, date, start, end, proc, pBilling, iBilling, tBill, payment):
    mydb = mysql.connector.connect(
        host = hostName,
        user=userName,
        password=passwordString,
        database=databaseName
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update patient_billing set billing_id = %s, date_of_visit = %s, start_time = %s, end_time = %s, procedure_ = %s,
    patient_portion = %s, insurance_portion = %s, total_billing = %s, pay = %s where billing_id = %s"""
    data = (date, start, end, proc, pBilling, iBilling, tBill, payment, id)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("final")
 
 
###HANDLES USER-----------------------------------------------------------
def userInsertion(id, password, ssn, fname, lname, address):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO user_ (USERID, PASSWORD_, SSN, FIRST_NAME, LAST_NAME, ADDRESS) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (id, password, ssn, fname, lname, address)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def userUpdate(id, password, ssn, fname, lname, address):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update user_ set PASSWORD_ = %s, SSN = %s, FIRST_NAME = %s, LAST_NAME = %s,
     ADDRESS = %s where USERID = %s"""
    data = (password, ssn, fname, lname, address, id)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")

###HANDLES RECORD-----------------------------------------------------------
def recordInsertion(id, price, type, dentist, notes):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO record (record_id, price, visit_type, assigned_dentist, additional_notes) VALUES (%s, %s, %s, %s, %s)"
    data = (id, price, type, dentist, notes)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("insert")
 
def recordUpdate(id, price, type, dentist, notes):
    mydb = mysql.connector.connect(
        host = hostName,
        database=databaseName,
        user=userName,
        password=passwordString
    )
    mycursor=mydb.cursor()
    sql_update_query = """Update record set price = %s, visit_type = %s, assigned_dentist = %s, additional_notes = %s where record_id = %s"""
    data = (price, type, dentist, notes, id)
    mycursor.execute(sql_update_query, data)
    mydb.commit()
    print("update final")
#-----------------------------------------------------------------------------
 
 
@receptionist.route('/receptionist/selection', methods=['GET', 'POST'])
def selection():
    return '''
        <p id="demo"></p>
        <h2>Hello, Please Choose What You Would Like to Do</h2>
 
        <button type="button" onclick="location.href='/receptionist/patient'">Patient Information</button>
        <button type="button" onclick="location.href='/receptionist/appointment'">Appointment Information</button><br>
 
        <button type="button" onclick="location.href='/receptionist/procedure'">Procedure Information</button>
        <button type="button" onclick="location.href='/receptionist/billing'">Billing Information</button><br>
 
        <button type="button" onclick="location.href='/receptionist/branch'">Branch Information</button>
        <button type="button" onclick="location.href='/receptionist/invoice'">Invoice Information</button><br>
        <button type="button" onclick="location.href='/receptionist/fee'">Fee Information</button>
        <button type="button" onclick="location.href='/receptionist/user'">User Information</button><br>
        <button type="button" onclick="location.href='/receptionist/employee'">Employee Information</button>
        <button type="button" onclick="location.href='/receptionist/record'">Record Information</button><br><br>
        <button type="button" onclick="location.href='/'">Home</button>
    </form>
</body>
</html>
    '''
 
@receptionist.route('/receptionist/patient', methods=['GET', 'POST'])
def patient():
    pID = request.form.get('pID')
    gID = request.form.get('gID')
    gender = request.form.get('gender')
    DoB = request.form.get('date')
    insurance = request.form.get('insurance')
    email = request.form.get('emailaddress')
    status = request.form.get('status')
    phone = request.form.get('phone')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            patientInsertion(pID, gID, gender, DoB, insurance, email, status)
            phoneInsertion(pID, phone)
        elif  request.form.get('Update') == 'Update':
            patientUpdate(pID, gID, gender, DoB, insurance, email, status)
            phoneInsertion(pID, phone)
        else:
            pass
   
    return '''
        <h2>Add and Update Patient Information</h2>
 
        <!-- change GET to POST (post works with servers) emailaddress, dateofbirth, age-->
        <form name="repPat" form action="" onsubmit="return validateForm()" method="POST">
        <label for="pID">Patient ID:</label>
        <input type="text" id="pID" name="pID" value=""><br><br>
 
        <label for="gID">Guardian ID:</label>
        <input type="text" id="gID" name="gID" value=""><br><br>
 
        <label for="gender">Gender:</label>
        <input type="text" id="gender" name="gender" value=""><br><br>
 
        <label for="date">Date of Birth:</label>
        <input type="date" id="date" name="date" value=""><br><br>
 
        <label for="insurance">Insurance:</label>
        <input type="text" id="insurance" name="insurance" value=""><br><br>
 
        <label for="emailaddress">Email Address:</label>
        <input type="text" id="emailaddress" name="emailaddress" value=""><br><br>
 
        <label for="status">Age Status:</label>
        <input type="text" id="status" name="status" value=""><br><br>
       
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" placeholder="123-45-678" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" required><br><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
</body>
</html>
    '''
 
@receptionist.route('/receptionist/employee', methods=['GET', 'POST'])
def employee():
    id = request.form.get('eID')
    role = request.form.get('role')
    salary = request.form.get('salary')
    branch = request.form.get('branch')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            employeeInsertion(id, role, salary, branch)
            locationInsertion(branch, id)
        elif  request.form.get('Update') == 'Update':
            employeeUpdate(id, role, salary, branch)
            locationInsertion(branch, id)
        else:
            pass
   
    return '''
        <h2>Add and Update Employee Information</h2>
 
        <!-- change GET to POST (post works with servers) emailaddress, dateofbirth, age-->
        <form name="repPat" form action="" onsubmit="return validateForm()" method="POST">
        <label for="eID">Employee ID:</label>
        <input type="text" id="eID" name="eID" value=""><br><br>
 
        <label for="role">Role:</label>
        <input type="text" id="role" name="role" value=""><br><br>
 
        <label for="salary">Salary:</label>
        <input type="text" id="salary" name="salary" value=""><br><br>
 
        <label for="branch">Branch ID:</label>
        <input type="text" id="branch" name="branch" value=""><br><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
</body>
</html>
    '''
 
 
 ##change
@receptionist.route('/receptionist/appointment', methods=['GET', 'POST'])
def appointment():
    id = request.form.get('id')
    start = request.form.get('start')
    end = request.form.get('end')
    dentist = request.form.get('dentist')
    date = request.form.get('date')
    patient = request.form.get('patient')
    appointmenttype = request.form.get('appointmenttype')
    status = request.form.get('status')
    record = request.form.get('record')
    invoice = request.form.get('invoice')
    room = request.form.get('room')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            appointmentInsertion(id, start, end, date, appointmenttype, status, room, patient, dentist, record, invoice)
        elif  request.form.get('Update') == 'Update':
            appointmentUpdate(id, start, end, date, appointmenttype, status, room, patient, dentist, record, invoice)
        else:
            pass
    return '''
        <h2>Add and Update Appointment Information</h2>
 
        <!-- change GET to POST (post works with servers) emailaddress, dateofbirth, age-->
        <form action="" method="POST">
        <label for="id">Appointment ID:</label>
        <input type="text" id="id" name="id" value=""><br><br>
 
        <label for="start">Start Time:</label>
        <input type="time" id="start" name="start" value=""><br><br>
 
        <label for="end">End Time:</label>
        <input type="time" id="end" name="end" value=""><br><br>
 
        <label for="dentist">Dentist:</label>
        <input type="text" id="dentist" name="dentist" value=""><br><br>
 
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" value=""><br><br>
 
        <label for="patient">Patient:</label>
        <input type="text" id="patient" name="patient" value=""><br><br>
 
        <label for="appointmenttype">Appointment Type:</label>
        <input type="text" id="appointmenttype" name="appointmenttype" value=""><br><br>
 
        <label for="status">Status of Visit:</label>
        <input type="text" id="status" name="status" value=""><br><br>
 
        <label for="record">Record:</label>
        <input type="text" id="record" name="record" value=""><br><br>
 
        <label for="invoice">Invoice:</label>
        <input type="text" id="invoice" name="invoice" value=""><br><br>
 
        <label for="room">Room:</label>
        <input type="text" id="room" name="room" value=""><br><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''
 
@receptionist.route('/receptionist/branch', methods=['GET', 'POST'])
def branch():
    id = request.form.get('id')
    city = request.form.get('city')
    manager = request.form.get('manager')
    recep1 = request.form.get('receptionist1')
    recep2 = request.form.get('receptionist2')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            branchInsertion(id, city, manager, recep1, recep2)
        elif  request.form.get('Update') == 'Update':
            branchUpdate(id, city, manager, recep1, recep2)
        else:
            pass
 
    return '''
    <h2>Add or Edit Branch Data</h2>
 
        <form method="POST">
        <label for="id">Branch ID:</label><br>
        <input type="text" id="id" name="id" value=""><br>
 
        <label for="manager">Manager:</label><br>
        <input type="text" id="manager" name="manager" value=""><br>
 
        <label for="city">City:</label><br>
        <input type="text" id="city" name="city" value=""><br>
 
        <label for="receptionist1">Receptionists:</label><br>
        <input type="text" id="receptionist1" name="receptionist1" value=""><br>
        <input type="text" id="receptionist2" name="receptionist2" value=""><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''
 ##change
@receptionist.route('/receptionist/procedure', methods=['GET', 'POST'])
def procedure():
    id = request.form.get('id')
    code = request.form.get('code')
    date = request.form.get('date')
    patient = request.form.get('patient')
    toothInvolved = request.form.get('toothInvolved')
 
    type = request.form.get('type')
    appointment = request.form.get('appointment')
    desc = request.form.get('desc')
    dose = request.form.get('dose')
    invoice = request.form.get('invoice')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            branchInsertion(id, code, date, patient, toothInvolved, type, appointment, desc, dose, invoice)
        elif  request.form.get('Update') == 'Update':
            branchUpdate(id, code, date, patient, toothInvolved, type, appointment, desc, dose, invoice)
        else:
            pass
 
    return '''
    <h2>Add or Edit Procedure Data</h2>
 
        <form method="POST">
        <label for="id">Procedure ID:</label><br>
        <input type="text" id="id" name="id" value=""><br>
 
        <label for="code">Procedure Code:</label><br>
        <input type="text" id="code" name="code" value=""><br>
 
        <label for="date">Date:</label><br>
        <input type="text" id="date" name="date" value=""><br>
 
        <label for="patient">Patient:</label><br>
        <input type="text" id="patient" name="patient" value=""><br>
 
        <label for="toothInvolved">Tooth Involved:</label><br>
        <input type="text" id="toothInvolved" name="toothInvolved" value=""><br>
       
        <label for="type">Procedure Type:</label><br>
        <input type="text" id="type" name="type" value=""><br>
 
        <label for="appointment">Appointment:</label><br>
        <input type="text" id="appointment" name="appointment" value=""><br>
       
        <label for="desc">Description:</label><br>
        <input type="text" id="desc" name="desc" value=""><br>
 
        <label for="dose">Dose Amount:</label><br>
        <input type="text" id="dose" name="dose" value=""><br>
       
        <label for="invoice">Invoice:</label><br>
        <input type="text" id="invoice" name="invoice" value=""><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''
 ##change
@receptionist.route('/receptionist/invoice', methods=['GET', 'POST'])
def invoice():
    iID = request.form.get('iID')
    DoI = request.form.get('date')
    contact = request.form.get('conInfo')
    pCharge = request.form.get('pCharge')
    iCharge = request.form.get('iCharge')
    pID = request.form.get('pID')

    penalty = request.form.get('penalty')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            invoiceInsertion(iID, pID, DoI, contact, pCharge, iCharge, penalty)
        elif request.form.get('Update') == 'Update':
            invoiceUpdate(iID, pID, DoI, contact, pCharge, iCharge, penalty)
        else:
            pass

    return '''
    <h2>Add or Edit Invoice Data</h2>

        <form method="POST">
        <label for="iID">Invoice ID:</label><br>
        <input type="text" id="iID" name="iID" value=""><br>

        <label for="pID">Patient ID:</label><br>
        <input type="text" id="pID" name="pID" value=""><br>

        <label for="date">Date of Issue:</label><br>
        <input type="date" id="date" name="date" value=""><br>

        <label for="conInfo">Contact Information (phone number):</label><br>
        <input type="tel" id="conInfo" name="conInfo" placeholder="123-45-678" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" required><br>

        <label for="pCharge">Patient Charge:</label><br>
        <input type="text" id="pCharge" name="pCharge" value=""><br>

        <label for="iCharge">Insurance Charge:</label><br>
        <input type="text" id="iCharge" name="iCharge" value=""><br>

        <label for="penalty">Penalty:</label><br>
        <input type="text" id="penalty" name="penalty" value=""><br><br>

        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''
 ##change
@receptionist.route('/receptionist/fee', methods=['GET', 'POST'])
def fee():
    feeID = request.form.get('feeID')
    procedure = request.form.get('procedure')
    code = request.form.get('code')
    charge = request.form.get('charge')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            feeInsertion(feeID, procedure, code, charge)
        elif  request.form.get('Update') == 'Update':
            feeUpdate(feeID, procedure, code, charge)
        else:
            pass
   
    return '''
    <h2>Add or Edit Fee Data</h2>
 
        <form name="repFee" form action="" onsubmit="return validateForm()" method="POST">
        <label for="feeID">Fee Identifier:</label><br>
        <input type="text" id="feeID" name="feeID" value=""><br>
 
        <label for="procedure">Procedure Type:</label><br>
        <input type="text" id="procedure" name="procedure" value=""><br>
 
        <label for="code">Fee Code:</label><br>
        <input type="text" id="code" name="code" value=""><br>
 
        <label for="charge">Charge:</label><br>
        <input type="text" id="charge" name="charge" value=""><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
</body>
</html>
    '''
 
 ##change NEEDS WORK
@receptionist.route('/receptionist/billing', methods=['GET', 'POST'])
def billing():
    id = request.form.get('id')
    date = request.form.get('date')
    start = request.form.get('start')
    end = request.form.get('end')
    pBilling = request.form.get('pBill')
    iBilling = request.form.get('iBill')
    tBill = 0
    proc = request.form.get('type')
    payment = request.form.get('pay')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            billingInsertion(id, date, start, end, proc, pBilling, iBilling, tBill, payment)
        elif  request.form.get('Update') == 'Update':
            billingUpdate(id, date, start, end, proc, pBilling, iBilling, tBill, payment)
        else:
            pass
 
    return '''
    <h2>Add or Edit Billing Data</h2>
 
        <form method="POST">
        <label for="id">Billing ID:</label><br>
        <input type="text" id="id" name="id" value=""><br>
 
        <label for="date">Date of Visit:</label><br>
        <input type="date" id="date" name="date" value=""><br>
 
        <label for="start">Start Time:</label><br>
        <input type="time" id="start" name="start" value=""><br>
 
        <label for="end">End Time:</label><br>
        <input type="time" id="end" name="end" value=""><br>
 
        <label for="type">Procedure Type:</label><br>
        <input type="text" id="type" name="type" value=""><br>
 
        <label for="pBill">Patient Billing:</label><br>
        <input type="text" id="pBill" name="pBill" value=""><br>
 
        <label for="iBill">Insurance Billing:</label><br>
        <input type="text" id="iBill" name="iBill" value=""><br>
       
        <label for="pay">Payment:</label><br>
        <input type="text" id="pay" name="pay" value=""><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''
@receptionist.route('/receptionist/user', methods=['GET', 'POST'])
def user():
    id = request.form.get('id')
    password = request.form.get('pass')
    ssn = request.form.get('ssn')
    fname = request.form.get('fName')
    lname = request.form.get('lName')
    address = request.form.get('address')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            userInsertion(id, password, ssn, fname, lname, address)
        elif  request.form.get('Update') == 'Update':
            userUpdate(id, password, ssn, fname, lname, address)
        else:
            pass
 
    return '''
    <h2>Add or Edit User Data</h2>
 
        <form method="POST">
        <label for="id">User ID:</label><br>
        <input type="text" id="id" name="id" value=""><br>
 
        <label for="pass">Password:</label><br>
        <input type="password" id="pass" name="pass" value=""><br>
 
        <label for="ssn">SSN:</label><br>
        <input type="text" id="ssn" name="ssn" value=""><br>
 
        <label for="fName">First Name:</label><br>
        <input type="text" id="fName" name="fName" value=""><br>
       
        <label for="lName">Last Name:</label><br>
        <input type="text" id="lName" name="lName" value=""><br>
       
        <label for="address">Address:</label><br>
        <input type="text" id="address" name="address" value=""><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''

@receptionist.route('/receptionist/record', methods=['GET', 'POST'])
def record():
    id = request.form.get('id')
    price = request.form.get('price')
    type = request.form.get('type')
    dentist = request.form.get('dentist')
    notes = request.form.get('notes')
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            recordInsertion(id, price, type, dentist, notes)
        elif  request.form.get('Update') == 'Update':
            recordUpdate(id, price, type, dentist, notes)
        else:
            pass
 
    return '''
    <h2>Add or Edit Record Data</h2>
 
        <form method="POST">
        <label for="id">Record ID:</label><br>
        <input type="text" id="id" name="id" value=""><br>
 
        <label for="price">Price:</label><br>
        <input type="text" id="price" name="price" value=""><br>
 
        <label for="type">Visit Type:</label><br>
        <input type="text" id="type" name="type" value=""><br>
       
        <label for="dentist">Assigned Dentist ID:</label><br>
        <input type="text" id="dentist" name="dentist" value=""><br>
       
        <label for="notes">Additional Notes:</label><br>
        <input type="text" id="notes" name="notes" value=""><br><br>
 
        <input type="submit" value="Add" name="Add">
        <input type="submit" value="Update" name="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''