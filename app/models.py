from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
     __tablename__ = 'users'
     
     id = db.Column(db.Integer,primary_key=True)
     username= db.Column(db.String(150),unique=True,nullable=False)
     email = db.Column(db.String(150),unique=True,nullable=False)
     password = db.Column(db.String(150),nullable=False)
     created_at = db.Column(db.DateTime,default=datetime.utcnow)
     tasks = db.relationship('Task',backref='owner',lazy=True)
     
     def __repr__ (self):
         return f"<User {self.username}>"

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    description = db.Column(db.String(500),nullable=True)
    status = db.Column(db.String(50),default='pending')
    created_at =db.Column(db.DateTime,default=datetime.utcnow)
    user_id =db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id
        }
    
    
     