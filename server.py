from flask import Flask, request, render_template
from flask import send_from_directory
import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="prasadv",
  passwd="sam",
  database='test',
  auth_plugin='mysql_native_password'
)

print(mydb)

app = Flask(__name__,template_folder='templates')

static_file_dir='html'

## CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(16), password VARCHAR(16));


#Simple Get Request
#Access with url http://localhost:5000/get
@app.route('/')
def index():
	return send_from_directory(static_file_dir, 'index.html')

#Simple Get Request
#Access with url http://localhost:5000/get
@app.route('/get')
def simple_get():
	return "Simple Get Request"

#Simple Get Request
#Access with url http://localhost:5000/getWithQueryParams?score=213
@app.route('/getWithQueryParams')
def get_with_query_params():
	if('score' in request.args):
		if(int(request.args['score'])>100):
			return "he has a century"
		else:
			return "he has hit "+str(request.args['score'])
	else:
		return "Please provide score as a query parameter."

@app.route('/createNewUser',methods = ['POST', 'GET'])
def create_new_user():
	if request.method == "GET":
		return send_from_directory(static_file_dir, 'registration.html')
	elif request.method == "POST":
		if 'username' in request.form:
			if 'password' in request.form:
				mycursor = mydb.cursor()
				query = "INSERT INTO users (username, password) VALUES (%s, %s)"
				mycursor.execute(query, (request.form['username'],request.form['password']))
				mydb.commit()
				return send_from_directory(static_file_dir, 'getUser.html')
			else:
				return send_from_directory(static_file_dir, 'registration.html')
		else:
			return send_from_directory(static_file_dir, 'registration.html')
	else:
		return "Invalid method"

@app.route('/users', methods=['GET'])
def get_user_page():
	return send_from_directory(static_file_dir, 'getUser.html')

@app.route('/users/<path:path>', methods=['GET'])
def get_user(path):
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM users where username='"+path+"'")
	myresult = mycursor.fetchall()
	if len(myresult)>0:
		rs=myresult[0]
		id=rs[0]
		username=rs[1]
		return render_template('getUser.html',username=username,id=id)
	else:
		return send_from_directory(static_file_dir, 'getUser.html')


# TO SERVE STATIC FILES from THE HTML FOLDER
@app.route('/static', methods=['GET'])
def serve_dir_directory_index():
	return send_from_directory(static_file_dir, 'index.html')

@app.route('/static/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
	if not os.path.isfile(os.path.join(static_file_dir, path)):
		path = os.path.join(path, 'index.html')
	return send_from_directory(static_file_dir, path)

if __name__ == '__main__':
	app.run()



