import psycopg2

class my_db:
    def __init__(self, db_name, user, password, cur, conn):
        self.db_name = db_name
        self.user_name = user
        self.password = password
        self.conn = psycopg2.connect("dbname=tracker_db user=user_1 password=database")
        self.cur = conn.cursor()
    
    def create_table():
        pass
