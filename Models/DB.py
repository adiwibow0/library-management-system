from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


class DB(object):
	"""Initialize mysql database """
	host = "localhost"
	user = "root"
<<<<<<< HEAD
<<<<<<< HEAD
	password = ''
=======
	password = ""
>>>>>>> 32f3469995594c201b7f3e137358280191a4ad84
=======
	password = ""
>>>>>>> 18ee8547c09bb23805da1e02dce7b83a073eace0
	db = "lms"
	table = ""

	def __init__(self, app):
		app.config["MYSQL_DATABASE_HOST"] = self.host;
		app.config["MYSQL_DATABASE_USER"] = self.user;
		app.config["MYSQL_DATABASE_PASSWORD"] = self.password;
		app.config["MYSQL_DATABASE_DB"] = self.db;

		self.mysql = MySQL(app, cursorclass=DictCursor)

	def cur(self):
		return self.mysql.get_db().cursor()

	def query(self, q):
		h = self.cur()
	
		if (len(self.table)>0):
			q = q.replace("@table", self.table)

		h.execute(q)

		return h

	def commit(self):
		self.query("COMMIT;")
