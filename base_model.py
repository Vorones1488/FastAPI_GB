from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Boolean, Text, MetaData, create_engine, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import databases
import sqlalchemy



Base = declarative_base()

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)

engine = create_engine(
DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata= sqlalchemy.MetaData() 

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    family = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(170))
    order = relationship('OrderTables', back_populates='user')


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name_product = Column(String(20))
    descript = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    prod_order = relationship('OrderTables', back_populates='product')


class OrderTables(Base):
    __tablename__ = 'order_tables'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_product = Column(Integer, ForeignKey('product.id'), nullable=False)
    data_order = Column(DATETIME, default=datetime.utcnow)
    status_order =Column(Boolean, default=True)
    user = relationship('Users', back_populates='order')
    product = relationship('Product', back_populates='prod_order')



Base.metadata.create_all(engine)

