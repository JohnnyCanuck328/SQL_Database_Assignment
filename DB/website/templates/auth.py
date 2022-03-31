from flask import Blueprint, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return '''
        <h2>Sign Up</h2>

        <!-- change GET to POST (post works with servers)-->
        <form action="/sign-up" method="POST">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" value=""><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" value=""><br><br>
        <input type="submit" value="Submit">
    </form>

</body>
</html>
    '''

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        conpassword = request.form.get('conpassword')
        
        #if len(fname) < 2:
         #   flash('Name is too short', category='error')
        #elif len(password) < 5:
         #   flash('Password is too weak', category='error')            
        #elif password != conpassword:
         #   flash('Passwords do not match', category='error')
        #else:
         #   flash('User successfully added', category='success')

    return '''
    <h2>Sign Up</h2>

        <form method="POST">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value=""><br>

        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value=""><br>

        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" value=""><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" value=""><br>

        <label for="conpassword">Confirm Password:</label><br>
        <input type="password" id="conpassword" name="conpassword" value=""><br>

        <label for="email">Email Address:</label><br>
        <input type="email" id="email" name="email" value=""><br><br>

        <input type="submit" value="Submit">
    </form>

</body>
</html>
    '''