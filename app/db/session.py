from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "sqlite:///./notifications.db"  # swap with Postgres if needed

# Example MySQL connection string 
DATABASE_URL = "mysql+pymysql://root:Mysql#123@localhost:3306/test"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
