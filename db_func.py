import sqlite3


class DbObject():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()

        # create tables...
        cmd = """CREATE TABLE IF NOT EXISTS tbl_users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login VARCHAR NOT NULL,
            name VARCHAR NOT NULL,
            email VARCHAR,
            passwd VARCHAR NOT NULL,
            active INTEGER NOT NULL)"""
        self.curs.execute(cmd)
        self.conn.commit()
        self.conn.close()

        # check if admin login already created...
        if(self.chk_login_pwd('admin', 'admin123') == 0):
            # insert default admin login
            self.ins_tbl_users('admin', 'Administrator',
                               'admin@myappdomain.com', 'admin123', 1)

    # insert into table tbl_B...
    def ins_tbl_users(self, login, name, email, passwd, active):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = """INSERT INTO tbl_users(login, name, email, passwd, active) 
                    VALUES(?,?,?,?,?)"""
        data_tuple = (login, name, email, passwd, active)
        self.curs.execute(sqltext, data_tuple)
        self.conn.commit()
        self.conn.close()

    def viw_tbl_users(self):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "SELECT * FROM tbl_users"
        self.curs.execute(sqltext)
        rows = self.curs.fetchall()
        self.conn.close()
        return rows

    def chk_login_pwd(self, login, pwd):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "SELECT EXISTS(SELECT 1 FROM tbl_users WHERE login='{}' AND passwd='{}' LIMIT 1)".format(
            login, pwd)
        self.curs.execute(sqltext)
        row = self.curs.fetchone()
        self.conn.close()
        return row[0]

    '''def trc_tbl_Q(self):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "DELETE FROM tbl_Q"
        self.curs.execute(sqltext)
        self.conn.commit()
        self.conn.close()
        return 1
        '''
