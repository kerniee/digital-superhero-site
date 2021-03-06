from flask_login import UserMixin
from app import db


# Not working unfortunately
# class FileStatus(db.Enum):
#     uploaded = 1
#     processing = 2
#     ready = 3


class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user_id, filename):
        self.user_id = user_id
        self.filename = filename

    def __repr__(self):
        return '<File %r>' % self.filename


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(120), unique=False)
    files = db.relationship('File', lazy=True)

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name
