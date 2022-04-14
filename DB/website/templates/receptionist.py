from flask import Blueprint, request, flash, redirect, url_for, request
#import js2py

import mysql.connector
from mysql.connector import Error
import pandas as pd

receptionist = Blueprint('receptionist', __name__)


#-----------------------------------------------------------------------------
#Database stuff
#HOST
# ec2-3-224-125-117.compute-1.amazonaws.com
#DATABASE 
# d1olnnmm3arjl1
#USER xtwhmialbflmvm

###Successfully connects to a local database
def testInsertion(fName, lName):
    mydb = mysql.connector.connect(
        host = "localhost",
        user="root",
        password="1qaz@WSX",
        database="school"
    )
    mycursor=mydb.cursor()
    mySql_insert_query = "INSERT INTO customers (fname, lname) VALUES (%s, %s)"
    data = (fName, lName)
    mycursor.execute(mySql_insert_query, data)
    mydb.commit()
    print("success")

#def testInsertion(fName, lName):
#    mydb = mysql.connector.connect(
#        host = "ec2-3-224-125-117.compute-1.amazonaws.com",
#        user="cqakclaggzefxd",
#        password="24f6fc5c74e43db32a2143f192f7bfd199abb9f9aed74706bf9ca8a93b41bbea",
#        database="dc01q4egnqo6ot"
#    )
#    mycursor=mydb.cursor()
#    mySql_insert_query = "INSERT INTO test (fname, lname) VALUES (%s, %s)"
#    data = (fName, lName)
#    mycursor.execute(mySql_insert_query, data)
#    mydb.commit()
#    print("success")

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
        <button type="button" onclick="location.href='/receptionist/fee'">Fee Information</button><br><br>
        <button type="button" onclick="location.href='/'">Home</button>
    </form>

<script>
    function validateForm() {
        let x = document.forms["myForm"]["fname"].value;
        if (x == "") {
            alert("Name must be filled out");
            return false;
        }
    }
</script>
</body>
</html>
    '''

@receptionist.route('/receptionist/patient', methods=['GET', 'POST'])
def patient():
    first_name = request.form.get('fName')
    last_name = request.form.get('lName')
    print(first_name, " ", last_name)
    if request.method == "POST":
        testInsertion(first_name, last_name)
    
    return '''
        <h2>Add and Update Patient Information</h2>

        <!-- change GET to POST (post works with servers) emailaddress, dateofbirth, age-->
        <form name="repPat" form action="" onsubmit="return validateForm()" method="POST">
        <label for="ssn">SSN:</label>
        <input type="text" id="ssn" name="ssn" value=""><br><br>
        <label for="fName">First Name:</label>
        <input type="text" id="fName" name="fName" value=""><br><br>
        <label for="lName">Last Name:</label>
        <input type="text" id="lName" name="lName" value=""><br><br>
        <label for="address">Home Address:</label>
        <input type="text" id="address" name="address" value=""><br><br>
        <label for="insurance">Insurance:</label>
        <input type="text" id="insurance" name="insurance" value=""><br><br>
        <label for="emailaddress">Email Address:</label>
        <input type="text" id="emailaddress" name="emailaddress" value=""><br><br>
        <label for="dateofbirth">Date of Birth:</label>
        <input type="text" id="dateofbirth" name="dateofbirth" value=""><br><br><br>
        <input type="submit" value="Add">
        <input type="submit" value="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>

<script>
    function validateForm() {
        let x = document.forms["myForm"]["fname"].value;
        if (x == "") {
            alert("Name must be filled out");
            return false;
        }
    }
</script>
</body>
</html>
    '''

@receptionist.route('/receptionist/appointment', methods=['GET', 'POST'])
def appointment():
        data = request.form
        return '''
        <h2>Add and Update Patient Information</h2>

        <!-- change GET to POST (post works with servers) emailaddress, dateofbirth, age-->
        <form action="/" method="POST">
        <label for="start">Start Time:</label>
        <input type="text" id="start" name="start" value=""><br><br>

        <label for="end">End Time:</label>
        <input type="text" id="end" name="end" value=""><br><br>

        <label for="dentist">Dentist:</label>
        <input type="text" id="dentist" name="dentist" value=""><br><br>

        <label for="date">Date:</label>
        <input type="text" id="date" name="date" value=""><br><br>

        <label for="patient">Patient:</label>
        <input type="text" id="patient" name="patient" value=""><br><br>

        <label for="appointmenttype">Appointment Type:</label>
        <input type="text" id="appointmenttype" name="appointmenttype" value=""><br><br>

        <label for="status">Status:</label>
        <input type="text" id="status" name="status" value=""><br><br>

        <label for="room">Room:</label>
        <input type="text" id="room" name="room" value=""><br><br><br>

        <input type="submit" value="Add">
        <input type="submit" value="Update"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>

</body>
</html>
    '''

@receptionist.route('/receptionist/branch', methods=['GET', 'POST'])
def branch():
    data = request.form

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

        <input type="submit" value="Add Branch">
        <input type="submit" value="Edit Branch"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>

</body>
</html>
    '''

@receptionist.route('/receptionist/procedure', methods=['GET', 'POST'])
def procedure():
    data = request.form
 
    return '''
    <h2>Add or Edit Procedure Data</h2>
 
        <form method="POST">
        <label for="code">Procedure Code:</label><br>
        <input type="text" id="code" name="code" value=""><br>
 
        <label for="patient">Patient:</label><br>
        <input type="text" id="patient" name="patient" value=""><br>
 
        <label for="date">Date:</label><br>
        <input type="text" id="date" name="date" value=""><br>
 
        <label for="type">Procedure Type:</label><br>
        <input type="text" id="type" name="type" value=""><br>
 
        <label for="desc">Description:</label><br>
        <input type="text" id="desc" name="desc" value=""><br>
 
        <label for="toothInvolved">Tooth Involved:</label><br>
        <input type="text" id="toothInvolved" name="toothInvolved" value=""><br>
 
        <label for="dose">Dose Amount:</label><br>
        <input type="text" id="dose" name="dose" value=""><br><br>
 
        <input type="submit" value="Add Procedure">
        <input type="submit" value="Edit Procedure"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''
 
@receptionist.route('/receptionist/invoice', methods=['GET', 'POST'])
def invoice():
    data = request.form
 
    return '''
    <h2>Add or Edit Invoic Data</h2>
 
        <form method="POST">
        <label for="treatID">Treatment ID:</label><br>
        <input type="text" id="treatID" name="treatID" value=""><br>
 
        <label for="date">Date of Issue:</label><br>
        <input type="text" id="date" name="date" value=""><br>
 
        <label for="conInfo">Contact Info:</label><br>
        <input type="text" id="conInfo" name="conInfo" value=""><br>
 
        <label for="pCharge">Patient Charge:</label><br>
        <input type="text" id="pCharge" name="pCharge" value=""><br>
 
        <label for="iCharge">Insurance Charge:</label><br>
        <input type="text" id="iCharge" name="iCharge" value=""><br>
 
        <label for="discount">Discount:</label><br>
        <input type="text" id="discount" name="discount" value=""><br>
 
        <label for="penalty">Penalty:</label><br>
        <input type="text" id="penalty" name="penalty" value=""><br>
 
        <label for="pInsur">Patient Insurance:</label><br>
        <input type="text" id="pInsur" name="pInsur" value=""><br><br>
 
        <input type="submit" value="Add Invoic">
        <input type="submit" value="Edit Invoic"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''
 
@receptionist.route('/receptionist/fee', methods=['GET', 'POST'])
def fee():
    data = request.form
    
    return '''
    <h2>Add or Edit Fee Data</h2>
 
        <form name="repFee" form action="test.php" onsubmit="return validateForm()" method="POST">
        <label for="feeID">Fee Identifier:</label><br>
        <input type="text" id="feeID" name="feeID" value=""><br>
 
        <label for="procedure">Procedure Type:</label><br>
        <input type="text" id="procedure" name="procedure" value=""><br>
 
        <label for="code">Fee Code:</label><br>
        <input type="text" id="code" name="code" value=""><br>
 
        <label for="charge">Charge:</label><br>
        <input type="text" id="charge" name="charge" value=""><br><br>
 
        <input type="submit" value="Add Fee">
        <input type="submit" value="Edit Fee"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
 <script>
    function validateForm() {
        let x = document.forms["myForm"]["fname"].value;
        if (x == "") {
            alert("Name must be filled out");
            return false;
        }
    }
</script>
</body>
</html>
    '''
 
@receptionist.route('/receptionist/billing', methods=['GET', 'POST'])
def billing():
    data = request.form
 
    return '''
    <h2>Add or Edit Billing Data</h2>
 
        <form method="POST">
        <label for="id">Billing ID:</label><br>
        <input type="text" id="id" name="id" value=""><br>
 
        <label for="date">Date of Visit:</label><br>
        <input type="text" id="date" name="date" value=""><br>
 
        <label for="start">Start Time:</label><br>
        <input type="text" id="start" name="start" value=""><br>
 
        <label for="end">End Time:</label><br>
        <input type="text" id="end" name="end" value=""><br>
 
        <label for="type">Procedure Type:</label><br>
        <input type="text" id="type" name="type" value=""><br>
 
        <label for="pBill">Patient Billing:</label><br>
        <input type="text" id="pBill" name="pBill" value=""><br>
 
        <label for="iBill">Insurance Billing:</label><br>
        <input type="text" id="iBill" name="iBill" value=""><br><br>
 
        <input type="submit" value="Add Billing">
        <input type="submit" value="Edit Billing"><br>
        <button type="button" onclick="location.href='/receptionist/selection'">Back</button>
    </form>
 
</body>
</html>
    '''




