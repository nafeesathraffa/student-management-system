from flask import Flask, render_template, url_for, flash, redirect
from forms import AddStudent
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e0a92ee969b28bb02155faa50a443e5a'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
  form = AddStudent()
  if form.validate_on_submit():
      flash(f'Added the Student {form.name.data} successfully!', 'success')
      return redirect(url_for('home'))
  return render_template('home.html',title='Student Mangement System', form=form)

if __name__ == "__main__":
  app.run(debug=True)