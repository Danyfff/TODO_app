from BD.base_manager import base_manager as db
from datetime import datetime

class Notes:
    
    def create_note(self, name, text, user_id):
        res = db.execute("INSERT INTO notes(name_notes, text, user_id, time_create, time_update) "
                        "VALUES (?, ?, ?, ?, ?)", 
                        args=(name, text, user_id, datetime.now(), datetime.now(), ))
        return res
        
    def get_notes(self, user_id):
        res = db.execute("SELECT *"
                        "FROM notes "
                        "WHERE user_id= ? ", 
                        args=(user_id, ))    
        return res
        
    def delete_note(self, id):
        res = db.execute("DELETE FROM notes WHERE id = ?", 
                        args=(id, ))    
        return res['code']
        
        
user = Notes()
print(user.get_notes(2))