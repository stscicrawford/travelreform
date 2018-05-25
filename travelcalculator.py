from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class CalculatorForm(Form):
    airfare = TextField('Airfare/Trainfare:', validators=[validators.required()])
    days_in_hotel = TextField('Number of days in HOTEL:', validators=[validators.required()])
    hotel_rate = TextField('HOTEL rate: the actual hotel rat if known or the GSA Daily Hotel Per DIem Rate', default ='$146.00', validators=[validators.required()])
    hotel_parking = TextField('HOTEL Parking rate per day:', default=0.0, validators=[validators.required()])
    meal_days = TextField('MEALS: Number of days:', validators=[validators.required()])
    meal_per_diem = TextField('MEALS: GSA MI&E Daily Per Diem rate:', validators=[validators.required()])
    rental_car = TextField('Rental Car:', validators=[validators.required()])
    other_car = TextField('OTHER: Mileage, Taxi, Gas, Tolls', validators=[validators.required()])
    other_phone= TextField('OTHER: Phone, internet', validators=[validators.required()])
    other_other = TextField('OTHER: Please explain in section E (below)', validators=[validators.required()])
    registration = TextField('Registration Fee:', validators=[validators.required()])

def remove_dollar(form_str):
    """Remove the dollar sign from a string and return a float"""
    return float(form_str.replace('$', ''))



@app.route("/calc", methods=['GET', 'POST'])
def trip_calc():
    calc = CalculatorForm(request.form)

    if request.method == 'POST':
        hotel_rate=request.form['hotel_rate']

        if calc.validate():
            # Save the comment here.
            registration = remove_dollar(request.form['registration'])
            total_airfare = remove_dollar(request.form['airfare'])
            total_hotel = int(request.form['days_in_hotel'])*remove_dollar(request.form['hotel_rate']) + remove_dollar(request.form['hotel_parking'])
            total_meals  = int(request.form['meal_days'])*remove_dollar(request.form['meal_per_diem'])
            total_other = remove_dollar(request.form['other_car']) + remove_dollar(request.form['other_phone']) + remove_dollar(request.form['other_other'])
            total_rate = registration + total_hotel + total_meals + total_other + total_airfare
            flash(f'Total Estimate Cost of Trip without Registration Fee:{total_rate - registration}')
            flash(f'Total Airfrare/Traainfare Estimate: {total_airfare}')
            flash(f'Total Hotel Estimate: {total_hotel}')
            flash(f'Total Meals Estimate: {total_meals}')
            flash(f'Total Other Estimate: {total_other}')
            flash(f'Registration Fee:{registration}')
            flash(f'Total Estimate Cost of Trip:{total_rate}')
        else:
            flash('All the form fields are required. ')

    return render_template('travelcalculator.html', form=calc)

if __name__ == "__main__":
    app.run()
