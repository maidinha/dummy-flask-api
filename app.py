from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#db = SQLAlchemy(app)

#DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user="postgres",pw="123456",url="127.0.0.1:5432",db="dummydb")

#app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# class TestModel(db.Model):
#     __tablename__ = "testmodels"

#     id = db.Column(db.Integer, primary_key = True)
#     description = db.Column(db.String(300), nullable=False)

#     def __init__ (self, id, description):
#         self.id = id
#         self.description = description

#     def __repr__(self):
#         return '<id {}>'.format(self.id)

@app.route('/')
def index():
    return "Hey! I'm working" 

@app.route('/get-data', methods=['GET'])
def get_all_models():
    return "Returning all models"

@app.route("/insert-data", methods=['POST'])
def insert_data():
    if request.is_json:
        incoming_data = request.get_json()
        return incoming_data.get('test')
    else:
        return "meh"
    
if __name__ == '__main_':
    app.run(debug=True, port=5000)