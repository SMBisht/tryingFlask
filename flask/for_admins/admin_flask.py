from sys import path as sys_path
from os import path as os_path

parent = os_path.abspath('..')
sys_path.insert(0,parent)

from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ggnt_db import Base, ggnt_tshirt_test 

engine_ggnt_db = create_engine('sqlite:///../ggnt.db')
Base.metadata.bind = engine_ggnt_db

DBSession =  sessionmaker(bind=engine_ggnt_db)
session = DBSession()
####################################################
## DB Session has been started from here ...
###################################################
app = Flask(__name__,template_folder="./admin_templates/",static_url_path="/static/")

@app.route('/common.css')
def return_css():
	return app.send_static_file('common.css')

@app.route('/admin')
@app.route('/admin/')
def admin_page():
	return render_template('admin_index.html')

@app.route('/admin/add-product')
@app.route('/admin/add-product/')
def admin_add_page():
	return render_template('add_product.html')

@app.route('/admin/add-product/t-shirt/test')
def add_test_tees():
	return render_template('add_test_tshirt.html')

@app.route('/admin/add-product/t-shirt/add-product-in-db',methods=['GET','POST'])
def add_prod_in_db():
	if request.method == 'POST':
		form = request.form
		#hidden fields from form:
		product_type = form['product_type'].encode('ascii','ignore')
		db_type = form['db_type'].encode('ascii','ignore')
		#filled form by admin:
		gender       = form['t_gender'].encode('ascii','ignore')
		category     = form['t_cat'].encode('ascii','ignore')
		subcategory  = form['t_sub'].encode('ascii','ignore')
		title        = form['t_title'].encode('ascii','ignore')
		description  = form['t_description'].encode('ascii','ignore')
		min_price    = int(form['t_min_price'].encode('ascii','ignore'))
		max_price    = int(form['t_max_price'].encode('ascii','ignore'))
		launch_price = int(form['t_launch_price'].encode('ascii','ignore'))
		small_url    = form['t_small_url'].encode('ascii','ignore')
		medium_url   = form['t_medium_url'].encode('ascii','ignore')
		large_url    = form['t_large_url'].encode('ascii','ignore')

		if product_type == "tshirt" and db_type=="test":
			new_test_tshirt = ggnt_tshirt_test(gender=gender,category=category,subcategory=subcategory,title=title,description=description,min_price=min_price,max_price=max_price,launch_price=launch_price,small_url=small_url,medium_url=medium_url,large_url=large_url)
			try:
				session.add(new_test_tshirt)
				session.commit()
			except:
				return "something went wrong!"
			first = session.query(ggnt_tshirt_test).first()
			print first.gender
	return "get"
@app.route('/admin/show-test-tshirts')
def show_all():
	tshirts = session.query(ggnt_tshirt_test).all()
	return render_template('show_test_tshirts.html',tshirts=tshirts)
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
