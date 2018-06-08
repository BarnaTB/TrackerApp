import psycopg2
import uuid


class Mydb:
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname='tracker_db' user='user_1' password='database' host='localhost' port='5432'")
        self.cur = self.conn.cursor()

    def close_conn(self):
        self.cur.close()

    def get_dbname(self):
        return self.dbname

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_conn(self):
        return self.conn

    def create_request_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS requests (id SERIAL, requesttype TEXT, category TEXT, details TEXT, email TEXT);")
        self.conn.commit()

    def crt_request(self, requesttype, category, details, current_user_email):
        self.create_request_table()
        self.cur.execute("INSERT INTO requests (requesttype, category, details, email) VALUES ('{}', '{}', '{}', '{}');".format(requesttype, category, details, current_user_email))
        self.conn.commit()
        self.close_conn()

    def get_all_requests(self, email):
        self.connect()
        self.cur.execute("SELECT * FROM requests WHERE email={};".format(email))
        _requests = self.cur.fetchall()
        self.close_conn()
        return _requests

    def get_single_request(self, email, requestid):
        self.cur.execute(
            "SELECT * FROM requests WHERE  email={} and id = '{}';".format(email, requestid))
        request = self.cur.fetchall()
        # self.close_conn()
        return request

    def modify_request(self, requestid, requesttype, category, details, email):
        # self.cur.execute("SELECT * FROM requests WHERE id = {};".format(requestid))
        self.cur.execute("UPDATE requests SET requesttype={} category={}, details={} WHERE id={} AND email={};".format(
            requestype, slf.category, details, requestid, email))
        self.close_conn()


class Userdb:
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname='tracker_db' user='user_1' password='database' host='localhost' port='5432'")
        self.cur = self.conn.cursor()

    def close_conn(self):
        self.cur.close()

    def create_user_table(self):
        # self.connect()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, password TEXT, role varchar(6));")
        self.conn.commit()

    def add_user(self, email, confirmPassword, role='user'):
        self.create_user_table()
        # self.connect()
        self.cur.execute("INSERT INTO users(email, Password, role) VALUES ('{}', '{}', {});".format(
            email, confirmPassword, role))
        self.conn.commit()
        self.close_conn()

    def get_user_by_email(self, email, password):
        self.cur.execute("SELECT email, password FROM users WHERE email='{}' AND password='{}';".format(email, password))
        self.conn.commit()
        row = self.cur.fetchall()
        if row is None:
            return None
        return row
