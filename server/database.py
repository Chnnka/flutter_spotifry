from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
DATABASE_URL='postgresql://postgres:admin@localhost:5432/flutter_musicapp'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine )
db= SessionLocal()