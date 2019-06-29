from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data.db')
Base = declarative_base()


class Prof(Base):
    __tablename__ = 'prof'
    id = Column(Integer, primary_key=True)
    language = Column(String(32))
    sql_developer = Column(Float)
    java_developer = Column(Float)
    data_scientist = Column(Float)
    data_engineer = Column(Float)
    backend_developer = Column(Float)
    frontend_developer = Column(Float)
    qa_engineer = Column(Float)
    databases_administrator = Column(Float)
    devops = Column(Float)
    javascript_developer = Column(Float)



Base.metadata.create_all(engine)

###
# from sqlalchemy.orm import Session
#
# session = Session(bind=engine)
#
# print(
#     session.query(Prof).first()
# )
