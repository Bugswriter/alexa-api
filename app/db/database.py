from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./site.db"
#SQLALCHEMY_DATABASE_URL = 'postgres://xtezipxz:3twTyHrhvQ-nXKoWeLuilGej3AaNjsCE@satao.db.elephantsql.com:5432/xtezipxz'
engine = create_engine( SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
