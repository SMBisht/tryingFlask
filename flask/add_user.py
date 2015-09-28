from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ggnt_db import Base, ggnt_user

def add_user_in_ggnt(Session,Name,Age,Email,Gender,Fname="",Lname="",DOB=0,PhoneNumber=0):
	new_user = ggnt_user(name=Name,age=Age,email=Email,gender=Gender,f_name=Fname,l_name=Lname,dob=DOB,phone_number=PhoneNumber)
	session.add(new_user)
	session.commit()

engine = create_engine('sqlite:///ggnt.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

add_user_in_ggnt(session,"shanu khera",24,"khera.shanu@gmail.com",0)

print session.query(ggnt_user).all()
