from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


#print("HTTP/1.0 200 OK\n")
#import cgi
#orm = cgi.FieldStorage()
#f_name=form["fName"].value
#s_name=form["lName"].value


#print("<br><b>First Name</b>",f_name)
#print("<br><b>Second Name</b>",s_name)
#print("<br><br><br><a href=form.htm>Back to Form</a>")