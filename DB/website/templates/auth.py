from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '''
        <h2>Sign Up</h2>

        <!-- change GET to POST -->
        <form action="results.html" method="GET">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value=""><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value=""><br><br>
        <input type="submit" value="Submit">
    </form>

</body>
</html>
    '''

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return '''
    <h2>Sign Up</h2>

        <form action="/action_page.php">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value=""><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value=""><br>
        <label for="email">Email Address:</label><br>
        <input type="text" id="email" name="email" value=""><br><br>
        <input type="submit" value="Submit">
    </form>

</body>
</html>
    '''