from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import AddStudent
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e0a92ee969b28bb02155faa50a443e5a'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:nafeesath008@localhost:5432/studentdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(20))
  dob = db.Column(db.Date)
  gender = db.Column(db.String(1))
  phone = db.Column(db.BigInteger)
  email = db.Column(db.String(20))
  address = db.Column(db.Text)
  coursedate = db.Column(db.Date)
  programname = db.Column(db.String(15))
  currsem = db.Column(db.Integer)

   

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
  form = AddStudent()

  

  if form.validate_on_submit():
      
    student = Student(
    id = form.studentId.data,
    name = form.name.data,
    dob = form.dob.data,
    gender = form.gender.data,
    phone = form.phoneNo.data,
    email = form.email.data,
    address = form.address.data,
    coursedate = form.courseDate.data,
    programname = form.programName.data,
    currsem = form.currentSem.data
    )

    db.session.add(student)
    db.session.commit()

    flash(f'Added the Student {form.name.data} successfully!', 'success')
    return redirect(url_for('home'))
  return render_template('home.html',title='Student Mangement System', form=form)

@app.route("/view")
def view():
  all_students = Student.query.all()
  return render_template("view.html", students=all_students)

if __name__ == "__main__":
  app.run(debug=True)