from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("aqlite:///study_tracker.db")

base_session = sessionmaker(engine)
local_session = base_session()

Base = declarative_base()


# Base.metadata.create_all()

