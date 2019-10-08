from databaseEngine import Base
from sqlalchemy import Column, Integer, String

class DummyData(Base):
    __tablename__ = "dummy_data"

    id = Column(Integer, primary_key = True)
    description = Column(String(300), nullable=False)

    def __init__ (self, id, description):
        self.id = id
        self.description = description

    def serialize(self):
       return {
           'id'         : self.id,
           'description': self.description,
       }
