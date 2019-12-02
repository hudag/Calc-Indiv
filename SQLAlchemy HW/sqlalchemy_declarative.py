import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'Customer'

    id = Column(Integer, primary_key=True)
    first_name= Column(String(250))
    last_name= Column(String(250))
    username= Column(String(250))
    email= Column(String(250))
    address= Column(String(250))
    town= Column(String(250))


class Item(Base):
    __tablename__ = 'Item'

    name= Column(Integer, primary_key=True)
    cost_price= Column(String(250))
    selling_price= Column(String(250))
    quantity = Column(String(250))

class Order(Base):
    __tablename__ = 'Order'

    order= Column(Integer, primary_key=True)
    item= Column(String(250))
    quantity= Column(String(250))

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.create_all(engine)