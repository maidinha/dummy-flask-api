from flask import Flask
from flask import request
from flask import Response
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user="postgres",pw="123456",url="127.0.0.1:5432",db="postgres")

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class DummyData(db.Model):
    __tablename__ = "dummy_data"

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(300), nullable=False)

    def __init__ (self, id, description):
        self.id = id
        self.description = description

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
       return {
           'id'         : self.id,
           'description': self.description,
       }

db.create_all()
db.session.commit()

@app.route('/')
def index():
    return "Hey! I'm working" 

@app.route('/get-dummy-data', methods=['GET'])
def get_all_dummy_data():
    query_data = DummyData.query.all()
    serialized_data = [DummyData.serialize(d) for d in query_data]
    jsonified_data = json.dumps({"dummy-data-set" : serialized_data}, indent=3)
    return Response(response=jsonified_data, status=200)

@app.route("/insert-dummy-data", methods=['POST'])
def process_dummy_data_insertion_request():
    if request.is_json:
        incoming_data = request.get_json()

        identifier = incoming_data.get("id")
        description = incoming_data.get("description")

        if is_invalid_dummy_data(identifier,description):
            return Response(response=build_error_message("Missing data at request content"), status=400)
        
        if insert_dummy_data(identifier,description):
            return Response(response=build_success_message("Data was inserted successfully"), status=200)
        else:
            return Response(response=build_error_message("There was some misterious error that happened, our programmers didn't have the time to specify it"), status=500)

    else:
        return Response(response=build_error_message("Not JSON Type"), status=400)

def build_error_message(message):
    return json.dumps({"error-message" : message})

def build_success_message(message):
    return  json.dumps({"success-message" : message})

def is_invalid_dummy_data(id, description):
    return not id or not description

def insert_dummy_data(identifier, desc):
    try:
        dummy_data = DummyData(id=identifier, description=desc)
        db.session.add(dummy_data)
        db.session.commit()
        return True
    except:
        return False
    

if __name__ == '__main_':
    app.run(debug=True, port=5000)