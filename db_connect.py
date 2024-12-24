from mysql.connector import connect


db = connect(
    host="localhost",
    user="azamat",
    password="27052705",
    database="Website_users",
)
db.autocommit = True
dbc = db.cursor()
