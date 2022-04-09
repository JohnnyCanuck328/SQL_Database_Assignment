from flask import Blueprint, request, flash

dentist = Blueprint('dentist', __name__)


@dentist.route('/dentist/appointment', methods=['GET', 'POST'])
def appointment():
    data = request.form
    print(data)
    return '''
        <h2>View Patient Information</h2>

        <!-- change GET to POST (post works with servers) emailaddress, dateofbirth, age-->
        <form method="GET">
        <label for="start">Start Time:</label>
        <input type="text" id="start" name="start" value="temporary text" readonly><br><br>

        <label for="end">End Time:</label>
        <input type="text" id="end" name="end" value="temporary text" readonly><br><br>

        <label for="dentist">Dentist:</label>
        <input type="text" id="dentist" name="dentist" value="temporary text" readonly><br><br>

        <label for="date">Date:</label>
        <input type="text" id="date" name="date" value="temporary text" readonly><br><br>

        <label for="patient">Patient:</label>
        <input type="text" id="patient" name="patient" value="temporary text" readonly><br><br>

        <label for="appointmenttype">Appointment Type:</label>
        <input type="text" id="appointmenttype" name="appointmenttype" value="temporary text" readonly><br><br>

        <label for="status">Status:</label>
        <input type="text" id="status" name="status" value="temporary text" readonly><br><br>

        <label for="room">Room:</label>
        <input type="text" id="room" name="room" value="temporary text" readonly><br><br><br>

    </form>

</body>
</html>
    '''
@dentist.route('/dentist/treatment', methods=['GET', 'POST'])
def treatment():
    data = request.form
 
    return '''
    <h2>View Treatments</h2>
 
        <form method="GET">
        <label for="treatment_ID">Treatment ID:</label>
        <input type="text" id="treatment_ID" name="treatment_ID" value="temporary text" readonly><br><br>
 
        <label for="dentist">Dentist:</label>
        <input type="text" id="dentist" name="dentist" value="temporary text" readonly><br><br>
 
        <label for="start_time">Start time:</label>
        <input type="text" id="start_time" name="start_time" value="temporary text" readonly><br><br>
 
        <label for="app_type">Appointment Type:</label>
        <input type="text" id="app_type" name="app_type" value="temporary text" readonly><br><br>
 
        <label for="trt_type">Treatment Type:</label>
        <input type="text" id="trt_type" name="trt_type" value="temporary text" readonly><br><br>
 
        <label for="medication">Medication:</label>
        <input type="text" id="medication" name="medication" value="temporary text" readonly><br><br>

        <label for="symptoms">Symptoms:</label>
        <input type="text" id="symptoms" name="symptoms" value="temporary text" readonly><br><br>
 
        <label for="toothInvolved">Tooth Involved:</label>
        <input type="text" id="toothInvolved" name="toothInvolved" value="temporary text" readonly><br><br>

        <label for="comments">Comments:</label>
        <input type="text" id="comments" name="comments" value="temporary text" readonly><br><br>
 
        <input type="submit" value="Appointment">
    </form>
 
</body>
</html>
    '''
 
@dentist.route('/dentist/procedure', methods=['GET', 'POST'])
def procedure():
    data = request.form
 
    return '''
    <h2>Add or Edit Procedure Data</h2>
 
        <form method="GET">
        <label for="code">Procedure Code:</label>
        <input type="text" id="code" name="code" value="temporary text" readonly><br><br>
 
        <label for="patient">Patient:</label>
        <input type="text" id="patient" name="patient" value="temporary text" readonly><br><br>
 
        <label for="date">Date:</label>
        <input type="text" id="date" name="date" value="temporary text" readonly><br><br>
 
        <label for="type">Procedure Type:</label>
        <input type="text" id="type" name="type" value="temporary text" readonly><br><br>
 
        <label for="desc">Description:</label>
        <input type="text" id="desc" name="desc" value="temporary text" readonly><br><br>
 
        <label for="toothInvolved">Tooth Involved:</label>
        <input type="text" id="toothInvolved" name="toothInvolved" value="temporary text" readonly><br><br>
 
        <label for="dose">Dose Amount:</label>
        <input type="text" id="dose" name="dose" value="temporary text" readonly><br><br>
 
        <input type="submit" value="Appointment">
    </form>
 
</body>
</html>
    '''

@dentist.route('/dentist/record', methods=['GET', 'POST'])
def record():
    data = request.form
 
    return '''
    <h2>Add or Edit Procedure Data</h2>
 
        <form method="GET">
        <label for="record_ID">Record ID:</label>
        <input type="text" id="record_ID" name="record_ID" value="temporary text" readonly><br><br>
 
        <label for="price">Price:</label>
        <input type="text" id="price" name="price" value="temporary text" readonly><br><br>
 
        <label for="visit_type">Visit Type:</label>
        <input type="text" id="visit_type" name="visit_type" value="temporary text" readonly><br><br>
 
        <label for="assigned_dentist">Assigned Dentist:</label>
        <input type="text" id="assigned_dentist" name="assigned_dentist" value="temporary text" readonly><br><br>
 
        <label for="addition_note">Additional Notes:</label>
        <input type="text" id="addition_note" name="addition_note" value="temporary text" readonly><br><br>
 
        <input type="submit" value="Appointment">
    </form>
 
</body>
</html>
    '''
 