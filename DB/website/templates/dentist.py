from flask import Blueprint, render_template, request, flash

dentist = Blueprint('dentist', __name__)


@dentist.route('/dentist/selection', methods=['GET', 'POST'])
def selection():
    return '''
        <h2>Hello, Please Choose What You Would Like to Do</h2>

        <button type="button" onclick="location.href='/dentist/appointment'">Appointment Information</button>
        <button type="button" onclick="location.href='/dentist/treatment'">Treatment Information</button><br>

        <button type="button" onclick="location.href='/dentist/procedure'">Procedure Information</button>
        <button type="button" onclick="location.href='/dentist/record'">Record Information</button><br><br>
        <button type="button" onclick="location.href='/'">Home</button>

    </form>

</body>
</html>
    '''


@dentist.route('/dentist/appointment', methods=['GET', 'POST'])
def appointment():
    data = request.form
    somedata = (("Rolf", "Software Engineer", "45000"),
               ("sponge", "Hardware Engineer", "120000"),
                ("Bob", "Mechanical Engineer", "40000"))

    return render_template("dentistAppointment.html", data = somedata)


@dentist.route('/dentist/treatment', methods=['GET', 'POST'])
def treatment():
    data = request.form

    return render_template("dentistTreatment.html")

@dentist.route('/dentist/procedure', methods=['GET', 'POST'])
def procedure():
    data = request.form

    return render_template("dentistProcedure.html")

@dentist.route('/dentist/record', methods=['GET', 'POST'])
def record():
    data = request.form

    return render_template("dentistRecord.html")