import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class ggnt_user(Base):
	__tablename__ = 'ggnt_user'

	id = Column(Integer, primary_key=True)
	name = Column(String(128),nullable=False)
	f_name = Column(String(64))
	l_name = Column(String(64))
	dob = Column(Integer,nullable=True)
	age = Column(Integer,nullable=False)
	email = Column(String(256),nullable=False,unique=True)
	phone_number = Column(Integer,nullable=True)
	gender = Column(Integer,nullable=False)

class ggnt_cart(Base):
	__tablename__ = 'ggnt_cart'

	id = Column(Integer,primary_key=True)
	product_1_id = Column(Integer,nullable=True)
	product_2_id = Column(Integer,nullable=True)
	product_3_id = Column(Integer,nullable=True)
	product_4_id = Column(Integer,nullable=True)
	product_5_id = Column(Integer,nullable=True)
	user_id = Column(Integer,ForeignKey('ggnt_user.id'))

class ggnt_tshirt_test(Base):

	__tablename__ = 'ggnt_tshirt_test'

	id = Column(Integer,primary_key=True)
	gender = Column(Enum('men','women','unisex','couples'))
	category = Column(Enum('tvshow'))
	subcategory = Column(Enum('friends'))
	title = Column(String(32))
	description = Column(String(128))
	min_price = Column(Integer)
	max_price = Column(Integer)
	launch_price = Column(Integer)
	small_url = Column(String(128))
	medium_url = Column(String(128))
	large_url = Column(String(128))

engine = create_engine("sqlite:///ggnt.db")
Base.metadata.create_all(engine)
