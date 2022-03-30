from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '''
<html>
<body>

<h1>Welcome</h1>
<h2>Please login or sign up</h2>

<button type="button" onclick="alert('Does nothing')">Login</button><br><br>
<button type="button" onclick="alert('Does nothing')">Sign Up</button>
 
</body>
</html>
    '''