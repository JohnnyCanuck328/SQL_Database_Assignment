from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '''
<html>
<body>

<h1>Welcome</h1>
<h2>Please login or sign up</h2>

<button type="button" onclick="location.href='/receptionist/selection'">Receptionist</button>
<button type="button" onclick="location.href='/dentist/login'">Dentist</button>
<button type="button" onclick="location.href='/patient/login'">Patient</button>
 
</body>
</html>
    '''