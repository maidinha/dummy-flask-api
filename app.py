from flask import Flask
from flask import request
from flask import Response
from dummyDataController import DummyDataController
from databaseEngine import Base, Engine
import json

myApp = Flask(__name__)

Base.metadata.create_all(Engine)

dummyController = DummyDataController()

@myApp.route('/')
def index():
    return "Hey! I'm working" 

@myApp.route('/get-dummy-data', methods=['GET'])
def get_all_dummy_data():
    query_result = dummyController.get_all_dummy_data()
    return Response(response=query_result, status=200)

@myApp.route("/insert-dummy-data", methods=['POST'])
def process_dummy_data_insertion_request():
    if request.is_json:
        incoming_data = request.get_json()

        identifier = incoming_data.get("id")
        description = incoming_data.get("description")

        if is_invalid_dummy_data(identifier,description):
            return Response(response=build_error_message("Missing data at request content"), status=400)
        
        if dummyController.insert_dummy_data(identifier,description):
            return Response(response=build_success_message("Data was inserted successfully"), status=200)
        else:
            return Response(response=build_error_message("There was some misterious error that happened, our programmers didn't have the time to specify it"), status=500)

    else:
        return Response(response=build_error_message("Not JSON Type"), status=400)

def is_invalid_dummy_data(id, description):
    return not id or not description

def build_error_message(message):
    return json.dumps({"error-message" : message})

def build_success_message(message):
    return  json.dumps({"success-message" : message})

if __name__ == '__main_':
    myApp.run(debug=True, port=5000)