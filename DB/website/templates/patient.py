from flask import Blueprint, render_template, request, flash

patient = Blueprint('patient', __name__)


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
    somedata = (("Rolf", "Software Engineer", "45000"),
               ("sponge", "Hardware Engineer", "120000"),
                ("Bob", "Mechanical Engineer", "40000"))

    return render_template("patientAppointment.html", data = somedata)


@patient.route('/patient/record', methods=['GET', 'POST'])
def record():
    data = request.form

    return render_template("patientRecord.html")

@patient.route('/patient/billing', methods=['GET', 'POST'])
def billing():
    data = request.form

    return render_template("patientBilling.html")
