from .BD.base_manager import base_manager as db

class User:
    
    id = int
    name = str
    
    """Создание пользователя"""
    def create_user(self, name, password):
        res = db.execute("INSERT INTO users(name, password) "
                        "VALUES (?, ?) ", 
                        args=(name, password, ), many=False)
        
        last = db.execute("SELECT id, name "
                          "FROM users "
                          "WHERE id= ? ", args=(res['lastrowid'], ), many=False)
        return {'code': res['code'], 'data': last['data']}
        
    def get_user(self, name):
        """Получение пользователя по id"""
        res = db.execute("SELECT id, name "
                        "FROM users "
                        "WHERE name= ? ", 
                        args=(name, ), many=False)    
        return res
    
    def check_user(self, name, password):
        """Проверка пользователя"""
        res = db.execute("SELECT id, name "
                        "FROM users "
                        "WHERE password= ? AND name = ? ", 
                        args=(password, name, ), many=False)    
        return res
    
    def get_all_users(self):
        """Получение всех пользователей"""
        res = db.execute("SELECT id, name "
                        "FROM users ")    
        return res
        
    def delete_user(self, id):
        """Удаление пользователя"""
        res = db.execute("DELETE FROM users WHERE id = ?", 
                        args=(id, ))
        return res['code']
        
    def activ_user(self, id, name):
        self.id = int(id)
        self.name = name

user = User()