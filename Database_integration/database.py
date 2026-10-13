from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Database_Url="sqlite:///./test.db"
engine=create_engine(
    Database_Url,connect_args={'check_same_thread':False}
)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()


