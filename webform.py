from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class TransportationForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    departure = TextField('Departure City:', validators=[validators.required()])
    arrival = TextField('Arrival City:', validators=[validators.required()])
    date_depart = TextField('Date of departure:', validators=[validators.required()])
    date_return = TextField('Date of return:', validators=[validators.required()])

    rental = SelectField('Is a rental car needed?', choices = [('yes','yes'), ('no', 'no')], validators = [validators.required()])
    hotel = SelectField('Is a hotel needed?', choices = [('yes','yes'), ('no', 'no')], validators = [validators.required()])


# @app.route("/", methods=['GET', 'POST'])
# def hello():
#     form = ReusableForm(request.form)
#
#     print(form.errors)
#     if request.method == 'POST':
#         name=request.form['name']
#         print(name)
#
#         if form.validate():
#             # Save the comment here.
#             flash('Hello ' + name)
#         else:
#             flash('All the form fields are required. ')
#
#     return render_template('webform.html', form=form)

@app.route("/", methods=['GET', 'POST'])
def transportation():
    form = TransportationForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        #General Transportation
        name = request.form['name']
        departure = request.form['departure']
        arrival = request.form['arrival']
        date_depart = request.form['date_depart']
        date_return = request.form['date_return']

        # Rental Car and Hotel
        rental = request.form['rental']
        hotel = request.form['hotel']
        # print(name)
        # print(departure)
        # print(arrival)
        # print(date_depart)
        # print(date_return)

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')

    return render_template('transportation.html', form=form)

if __name__ == "__main__":
    app.run()
