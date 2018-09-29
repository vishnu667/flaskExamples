

## Installation instructions 

### Dependencies:

Install python & pip & mysql

and pip dependencies `flask` & `MySQL-connector-python`
```
pip install flask
pip install MySQL-connector-python
```



setup Mysql Database and enter the credentials in server.py

```
mydb = mysql.connector.connect(
  host="localhost",
  user="prasadv",
  passwd="sam",
  database='test',
  auth_plugin='mysql_native_password'
)
```

### Running the Server


`python server.py`


API Urls 

GET Requests

* http://localhost:5000/
* http://localhost:5000/get
* http://localhost:5000/getWithQueryParams
* http://localhost:5000/getWithQueryParams?score=213
* http://localhost:5000/createNewUser
* http://localhost:5000/users
* http://localhost:5000/users/username
* http://localhost:5000/static
* http://localhost:5000/static/fileName


POST Requests

* http://localhost:5000/createNewUser


