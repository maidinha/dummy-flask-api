from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#The safe way is to declare this in a envinroment variable or in a file, but it wasn't made due to the time window 
DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user="postgres",pw="123456",url="127.0.0.1:5432",db="postgres")

Base = declarative_base()
Engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=Engine)
