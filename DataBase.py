import sqlite3

class DB:
    @staticmethod
    def execute_res(text, cur):
        rows = cur.execute(text)
        return rows
    
    @staticmethod
    def execute(text, cur, conn):
        cur.execute(text)
        conn.commit()

    @staticmethod
    def create_table():
        conn = sqlite3.connect('bot_db.sqlite')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            sclad INT,
            name TEXT,
            code TEXT,
            count INT
        );""")

        conn.commit()
        cur.close()
        conn.close()

        print('Таблицы успешно созданы!')
    
    @staticmethod
    def close_conn(conn, cur):
        conn.commit()
        cur.close()
        conn.close()
    
    @staticmethod
    def open_conn():
        conn = sqlite3.connect('bot_db.sqlite')
        cur = conn.cursor()
        return conn, cur
    
    @classmethod
    def get_info(cls, text):
        conn, cur = cls.open_conn()
        data = []
        rows = cls.execute_res(text=text, cur=cur)
        for row in rows:
            data.append(row)
        cls.close_conn(conn, cur)
        return data
    
    @classmethod
    def update_info(cls, count, name, sclad):
        conn, cur = cls.open_conn()
        cls.execute(text=f"UPDATE users SET count={count} WHERE name='{name}' AND sclad={sclad}", cur=cur, conn=conn)
        cls.close_conn(conn, cur)
    
    @classmethod
    def inser_info(cls, count, name, sclad, code):
        conn, cur = cls.open_conn()
        cls.execute(text=f"INSERT INTO users(sclad, name, code, count) VALUES ('{sclad}','{name}','{code}','{count}')", conn=conn, cur=cur)
        cls.close_conn(conn=conn, cur=cur)

    @classmethod
    def get_len(cls, sclad):
        conn, cur = cls.open_conn()
        data = []
        rows = cls.execute_res(text=f"SELECT * FROM users WHERE sclad={sclad}", cur=cur)
        for row in rows:
            data.append(row)
        cls.close_conn(conn, cur)
        return data