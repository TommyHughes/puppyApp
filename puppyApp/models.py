from puppyApp import db

class Puppy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=True)

    def __repr__(self):
        return f"Puppy('{self.id}','{self.name}')"

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Owner('{self.id}','{self.name}')"

class Toy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Toy('{self.id}','{self.type}')"