from flask import Flask, render_template,redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired, URL
import csv
from csv import writer
from markupsafe import Markup
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class CafeForm(FlaskForm):
    Cafe = StringField('Cafe name', validators=[DataRequired()])
    Location = StringField('Location', validators=[DataRequired(),URL()])
    Open = StringField('Opening Time', validators=[DataRequired()])
    Close = StringField('Closing time', validators=[DataRequired()])
    Coffee = SelectField('Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    Wifi = SelectField('Wifi Strength', choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪','✘'])
    Power = SelectField('Electricity', choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌','✘'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/adds', methods=["GET", "POST"])
def add_cafe():
    forms = CafeForm()
    if forms.validate_on_submit():
        with open("cafe-data.csv", mode="a",encoding="utf8") as csv_file:
            csv_file.write(f"\n{forms.Cafe.data},"
                           f"{forms.Location.data},"
                           f"{forms.Open.data},"
                           f"{forms.Close.data},"
                           f"{forms.Coffee.data},"
                           f"{forms.Wifi.data},"
                           f"{forms.Power.data}")
            return redirect(url_for('cafe'))
    return render_template('add.html', form=forms)


@app.route('/cafes')
def cafe():
    with open('cafe-data.csv', newline='',encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
