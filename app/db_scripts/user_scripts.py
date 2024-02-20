from BD.base_manager import base_manager as db

class User:
    def create_user(self, name):
        res = db.execute("INSERT INTO users(name) "
                        "VALUES (?) ", 
                        args=(name, ), many=False)
        
        last = db.execute("SELECT id, name "
                          "FROM users "
                          "WHERE id= ? ", args=(res['lastrowid'], ), many=False)
        return {'code': res['code'], 'data': last['data']}
        
    def get_user(self, name):
        res = db.execute("SELECT id, name "
                        "FROM users "
                        "WHERE name= ? ", 
                        args=(name, ), many=False)    
        return res
    
    def get_all_users(self):
        res = db.execute("SELECT * "
                        "FROM users ")    
        return res
        
    def delete_user(self, id):
        res = db.execute("DELETE FROM users WHERE id = ?", 
                        args=(id, ))
        return res['code']
        
        
user = User()
print(user.create_user('Вова'))
