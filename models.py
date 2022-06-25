from flask_sqlalchemy import SQLAlchemy

#instacia de sqlalchemy
db = SQLAlchemy()

#####################################
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(20),nullable=False)
    favorites=db.relationship('Favorite',backref="user", lazy=True)

    def __repr__(self):
        return "<User %r>" % self.name

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "password": self.password
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)

    def __repr__(self):
        return "<Favorite %r>" % self.id #no se cual va aqui

    def serialize(self):
        return {
            "id":self.id,
            "user_id": self.user_id
        }

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    episode = db.Column(db.String(250),nullable=False)
    name = db.Column(db.String(250),nullable=False)
    character = db.Column(db.String(250),nullable=False)
    air_date=db.Column(db.String(250)) 
    favorite = db.relationship('Favorite', backref='episode', lazy=True) 

    def __repr__(self):
        return "<Episode %r>" % self.name #no se cual va aqui

    def serialize(self):
        return {
            "id":self.id,
            "episode": self.episode,
            "name": self.name,
            "character": self.character,
            "air_date": self.air_date
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(50))
    episode = db.Column(db.String(250))
    gender=db.Column(db.String(250))  
    species=db.Column(db.String(250))  
    location=db.Column(db.String(250))
    favorite = db.relationship('Favorite', backref='character', lazy=True)   

    def __repr__(self):
        return "<Character %r>" % self.name 

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "status": self.status,
            "episode": self.episode,
            "gender": self.gender,
            "species": self.species,
            "location": self.location,
        }
