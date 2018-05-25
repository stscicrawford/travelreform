from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField, DateField


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class TransportationForm(Form):
    departure = TextField('Departure City:', validators=[validators.InputRequired()])
    arrival = TextField('Arrival City:', validators=[validators.InputRequired()])
    date_depart = DateField('Date of departure (mm/dd/yyyy):', format='%m/%d/%y',
                            validators=[validators.InputRequired()])
    date_return = DateField('Date of return (mm/dd/yyyy):', format='%m/%d/%y',
                            validators=[validators.InputRequired()])

    rental = SelectField('Is a rental car needed?',
                         choices=[('no_rental', 'No'), ('yes_rental','Yes')],
                         validators=[validators.InputRequired()])
    hotel = SelectField('Is a hotel needed?',
                        choices=[('no_hotel', 'No'), ('yes_hotel','Yes')],
                        validators=[validators.InputRequired()])
    other = TextField('Other (special requests):')
    comments = TextAreaField('Comments:', [validators.Length(max=500)])


@app.route("/", methods=['GET', 'POST'])
def transportation():
    form = TransportationForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        #General Transportation
        departure = request.form['departure']
        arrival = request.form['arrival']
        date_depart = request.form['date_depart']
        date_return = request.form['date_return']

        # Rental Car and Hotel
        rental = request.form['rental']
        hotel = request.form['hotel']

        other = request.form['other']
        comments = request.form['comments']

        print(departure)

        if form.validate():
            # Save the comment here.
            flash('Hello ')
        else:
            flash('All the form fields are required. ')

    return render_template('transportation.html', form=form)

if __name__ == "__main__":
    app.run()
