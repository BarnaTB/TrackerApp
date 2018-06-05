import psycopg2

class my_db:
    def __init__(self, dbname, user, password, conn):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn = psycopg2.connect("dbname=tracker_db user=user_1 password=database")
        self.cur = conn.cursor()
    
    def get_dbname(self):
        return self.dbname

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_conn(self):
        return self.conn