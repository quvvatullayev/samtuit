from tinydb import TinyDB, Query
# import Document
from tinydb.database import Document

class DB:
    """
        DB sxema
        {
            "chat_id": 123456789,
            "jop_name": "jop_name",
        }
    """
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.table = self.db.table("jobs")
        self.table = self.db.table("admin")
        self.query = Query()
        
    def add_job(self, chat_id, job_name):
        if self.table.get(doc_id=chat_id):
            return False
        else:
            self.table.insert(Document({"chat_id": chat_id, "job_name": job_name}, doc_id=chat_id))
            return True

    def add_admin(self, chat_id):
        if self.table.get(doc_id=chat_id):
            return False
        else:
            self.table.insert(Document({"chat_id": chat_id}, doc_id=chat_id))
            return True
        
    def get_job(self, chat_id):
        return self.table.get(doc_id=chat_id)
    
    def get_admin(self, chat_id):
        return self.table.get(doc_id=chat_id)
    
    def get_all_jobs(self):
        return self.table.all()
    
    def get_all_admins(self):
        return self.table.all()
