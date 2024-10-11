#Flask Application and the API Endpoints for handling HTTP requests
from flask import Flask, request, jsonify
from models import db, DataModel

app = Flask(__name__)  #Creation of Flask application

SERVER='localhost'
DATABASE='FLASKDB_NEW'
DRIVER='ODBC Driver 18 for SQL Server'

app.config['SQLALCHEMY_DATABASE_URI'] = (f"mssql+pyodbc://{SERVER}/{DATABASE}?driver={DRIVER}&Trusted_Connection=yes&TrustServerCertificate=yes")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  #initializes the db instance with the Flask application to configure SQLAlchemy with Flask App

@app.route('/product', methods=['POST'])
def add_product():
    if request.is_json:  #checks if data is in json format
        data = request.get_json()  #extracts the json data and returns to a dictionary

        entry_point = DataModel(
            name=data['name'],
            price=data['price'],
            discount=data['discount'],
            old_price=data['old_price']
        )
        db.session.add(entry_point)
        db.session.commit()  #inserts into SQL DB

        return jsonify({"message": "Data Added"}), 201
    else:
        return jsonify({"Error": "Invalid Request"}), 400


@app.route('/products', methods=['POST'])
def add_products():
    if request.is_json:  #checks if data is in json format
        data = request.get_json()  #extracts the json array and returns to a dictionary
        for item in data:
            entry_point = DataModel(
                name=item['Name'],
                price=item['Price'],
                discount=item['Discount'],
                old_price=item['Old Price']
            )
            db.session.add(entry_point)
            db.session.commit()  #inserts into SQL DB

        return jsonify({"message": "Data Added"}), 201
    else:
        return jsonify({"Error": "Invalid Request"}), 400


if __name__ == '__main__':
    app.run(debug=True)
