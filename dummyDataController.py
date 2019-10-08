from dummyDataModel import DummyData
from databaseEngine import Session
import json

class DummyDataController:

    session = Session()

    def get_all_dummy_data(self):
        query_data = self.session.query(DummyData).all()
        serialized_data = [DummyData.serialize(d) for d in query_data]
        jsonified_data = json.dumps({"dummy-data-set" : serialized_data}, indent=3)
        return jsonified_data
    
    def insert_dummy_data(self, identifier, desc):
        try:
            dummy_data = DummyData(id=identifier, description=desc)
            self.session.add(dummy_data)
            self.session.commit()
            return True
        except:
            return False
