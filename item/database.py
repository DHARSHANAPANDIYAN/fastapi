from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



url = "postgresql+psycopg2://freshers_dev_user:dkikKEvqVyRDpL3@mrpl-ace-hires.cukiszzh1lyw.ap-south-1.rds.amazonaws.com:5432/mrpl"

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()