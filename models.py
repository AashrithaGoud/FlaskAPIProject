#defines the structure of the data model that corresponds to the Products table in the DB

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() #Creates an ORM interface to connect your Python models with your SQL database tables.

class DataModel(db.Model): #A base class provided by SQLAlchemy, which links this Python class to a database table.
    __tablename__ = 'Stg_Products' #Table name in SQL Server
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    discount = db.Column(db.String(100), nullable=False)
    old_price = db.Column(db.String(100), nullable=False)

    def __init__(self, name, price, discount, old_price):
        self.name = name
        self.price = price
        self.discount = discount
        self.old_price = old_price
