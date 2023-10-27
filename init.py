from flask import Flask,render_template,request,redirect
import os
import uuid
import csv
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/shash/project101/project101.db"
db=SQLAlchemy()
db.init_app(app)
class demo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(200))
    lastname=db.Column(db.String(200))
    phone=db.Column(db.Integer)
    message=db.Column(db.String(200))
    address=db.Column(db.String(200))

    
    


@app.route('/get/')
def get():
    return session.get('key', 'not set')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/cards")
def cards():
    return render_template('cards.html')


@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/dev")
def dev():
    return render_template('dev.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/upload", methods=['GET','POST'])
def upload():
    if request.method=='POST':
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
       
        phone = request.form.get("phone")
        email = request.form.get("email")
        message = request.form.get("message")
        
        address = request.form.get("address")

        new_node=demo(firstname=firstname,lastname=lastname,phone=phone,message=message,address=address)
        db.session.add(new_node)
        db.session.commit() 
        



        data=request.form.to_dict()
        print(data)
        
        write(data)
        return render_template("thankyou.html",dname = firstname,dlname = lastname,dph = phone,demail = email,message = message,address = address)


def write(data):
    firstname=data['firstname']
    lastname=data['lastname']
    email=data['email']
    phone = data['phone']
    message = data['message']
    address = data['address']


            

        

    with open('database.csv', 'a', newline='') as csvfile:
      csv_writer= csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([firstname,lastname,email,phone,message,address])

           
           # key=uuid.uuid1()

        
        
        #Image Uploading Method
       #img = request.files["dp"]
        #img.save(f"static/images/{img.filename}")
        #img_new_name = f"{key}{img.filename}"
        #os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")


if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)