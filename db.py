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
        self.jobs = self.db.table("jobs")
        self.admin = self.db.table("admin")
        self.query = Query()
        
    def add_job(self, chat_id, job_name):
        if self.jobs.get(doc_id=chat_id):
            return False
        else:
            self.jobs.insert(Document({"chat_id": chat_id, "job_name": job_name}, doc_id=chat_id))
            return True

    def add_admin(self, chat_id):
        if self.admin.get(doc_id=chat_id):
            return False
        else:
            self.admin.insert(Document({"chat_id": chat_id}, doc_id=chat_id))
            return True
        
    def get_job(self, chat_id):
        return self.jobs.get(doc_id=chat_id)
    
    def get_admin(self, chat_id):
        return self.admin.get(doc_id=chat_id)
    
    def get_all_jobs(self):
        return self.jobs.all()
    
    def get_all_admins(self):
        return self.admin.all()
