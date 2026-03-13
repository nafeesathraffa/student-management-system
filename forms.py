from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class AddStudent(FlaskForm):
  studentId = IntegerField('Student Id', 
                           validators=[DataRequired()])
  name = StringField('Name', 
                     validators=[DataRequired(), Length(min=5, max=20)])
  dob = DateField('Date of Birth',
                  validators=[DataRequired()])
  gender = SelectField('Gender',
                       choices=[
                         ('M', 'Male'),
                         ('F', 'Female')
                       ],
                       validators=[DataRequired()])
  phoneNo = IntegerField('Phone No', 
                         validators=[DataRequired()])
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  address = TextAreaField('Address',
                          validators=[DataRequired()])
  courseDate = DateField('Course Date', 
                         validators=[DataRequired()])
  programName = StringField('Program Name',
                             validators=[DataRequired()])
  currentSem = SelectField('Current Semester',
                       choices=[
                         (0, '0'),
                         (1, '1'),
                         (2, '2'),
                         (3, '3'),
                         (4, '4'),
                         (5, '5'),
                         (6, '6'),
                         (7, '7'),
                         (8, '8')
                       ],
                       validators=[DataRequired()])
  submit = SubmitField('Submit')

  
  