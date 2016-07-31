from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60))
    is_active = db.Column(db.Boolean(), default=True)

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return str(self.id)
