from .BD.base_manager import base_manager as db
from datetime import datetime

class NotesBD:
    
    """Создание заметки"""
    def create_note(self, name, text, user_id):
        res = db.execute("INSERT INTO notes(name_notes, text, user_id, time_create, time_update) "
                        "VALUES (?, ?, ?, ?, ?)", 
                        args=(name, text, user_id, datetime.now(), datetime.now(), ))
        return res
    
    """Получение всех заметок по id пользователя"""
    def get_notes(self, user_id):
        res = db.execute("SELECT id, name_notes, text, time_create, time_update "
                        "FROM notes "
                        "WHERE user_id= ? ", 
                        args=(user_id, ))    
        return res
    
        """Получение всех заметок"""
    def get_all_notes(self):
        res = db.execute("SELECT * "
                        "FROM notes ")    
        return res
    
    """Удаление заметки"""
    def delete_note(self, id):
        res = db.execute("DELETE FROM notes WHERE id = ?", 
                        args=(id, ))    
        return res['code']
        
        
note = NotesBD()
