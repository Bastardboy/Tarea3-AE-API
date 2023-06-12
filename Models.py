from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model):
    __tablename__= 'Admin'
    rowid= db.Column(db.Integer, primary_key=True)
    Username= db.Column(db.String(200), unique=True)
    Password= db.Column(db.String(200), unique=True)
    def __repr__(self):
        return '<User %r>' % self.Username
    def set_password(self, password):
        self.Password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.Password, password)


class Company(db.Model):
    __tablename__= 'Company'
    ID= db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    company_name= db.Column(db.String(200), nullable=False)
    company_api_key= db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return '<Company %r>' % self.company_name
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def generate_token(self):
        pass


class Location(db.Model):
    __tablename__= 'Location'
    ID= db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    company_id= db.Column(db.Integer, db.ForeignKey('Company.ID'), nullable=False)
    location_name= db.Column(db.String(200), nullable=False)
    location_country= db.Column(db.String(200), nullable=False)
    location_city= db.Column(db.String(200), nullable=False)
    location_meta= db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return '<Location %r>' % self.location_name
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def generate_token(self):
        pass
    def to_json(self):
        return {
            "id": self.ID,
            "company_id": self.company_id,
            "location_name": self.location_name,
            "location_country": self.location_country,
            "location_city": self.location_city,
            "location_meta": self.location_meta
        }


class Sensor(db.Model):
    __tablename__= 'Sensor'
    sensor_id= db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    location_id= db.Column(db.Integer, db.ForeignKey('Location.ID'), nullable=False)
    sensor_name= db.Column(db.String(200), nullable=False)
    sensor_category= db.Column(db.String(200), nullable=False)
    sensor_meta= db.Column(db.String(200))
    sensor_api_key= db.Column(db.String(200))
    def __repr__(self):
        return '<Sensor %r>' % self.sensor_name
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def generate_token(self):
        pass
    def to_json(self):
        return {
            "sensor_id": self.sensor_id,
            "location_id": self.location_id,
            "sensor_name": self.sensor_name,
            "sensor_category": self.sensor_category,
            "sensor_meta": self.sensor_meta,
            "sensor_api_key": self.sensor_api_key
        }


class SensorData(db.Model):
    __tablename__= 'SensorData'
    sensor_data_id= db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    sensor_id= db.Column(db.Integer, db.ForeignKey('Sensor.sensor_id'), nullable=False)
    data= db.Column(db.String(200))
    date= db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<SensorData %r>' % self.data
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def generate_token(self):
        pass
    def to_json(self):
        return {
            "sensor_data_id": self.sensor_data_id,
            "sensor_id": self.sensor_id,
            "data": self.data
        }
    #timestamp between 2 dates in epoch time
    def timestamp_between(self, start, end):
        if self.date >= start and self.date <= end:
            return True
        