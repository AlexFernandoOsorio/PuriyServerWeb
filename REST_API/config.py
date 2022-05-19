from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations

app.config['MYSQL_DATABASE_USER'] = 'alex'
app.config['MYSQL_DATABASE_PASSWORD'] = 'topcat123'
app.config['MYSQL_DATABASE_DB'] = 'PuriyDatabase'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)