from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URl = "postgresql+psycopg2://postgres:2019@localhost:5432/shop"

engine = create_engine(DATABASE_URl)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()