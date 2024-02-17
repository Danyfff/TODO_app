import sqlite3
import os
from .settings import DB_PATH, DB_SCRIPTS_PATH


class DBManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        if not self.check_base():
            self.create_base()
        print('Create DBManager')

    def check_base(self) -> bool:
        return os.path.exists(self.db_path)

    def connect_to_base(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn, cur

    def create_base(self):
        conn, cur = self.connect_to_base()
        try:
            cur.executescript(open(DB_SCRIPTS_PATH).read())
            conn.commit()
            print('Tables are created')
        except sqlite3.Error as ex:
            print(ex)
        finally:
            conn.close()

    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_to_base()
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            return {"code": 200, "data": result}
        except sqlite3.Error as er:
            print(str(er))
            return {"code": 400}
        finally:
            conn.close()
            

base_manager = DBManager(DB_PATH)