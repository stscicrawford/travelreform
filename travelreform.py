from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, SelectField
from wtforms import validators, StringField, SubmitField, DateField
from wtforms import IntegerField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
wbs_flag = False

class TravelAdvance(Form):
    need_advance = TextField('Do you need a travel advance?', validators=[validators.required()])
    how_much_advance = TextField('How much?')
    any_part_personal = TextField('Is any part of this trip personal?', validators=[validators.required()])
    personal_travel_dates = DateField('If so, specify dates:')
    personal_travel_destination = TextField('If so, specify destination:')


class BasicInfoForm(Form):
    name = TextField('Name of Traveler:', validators=[validators.required()])
    title = TextField('Traveler Title:', validators=[validators.required()])
    phone = TextField('Phone:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])
    date_start = DateField('Start Date:',
                           format='%m/%d/%Y',
                           validators=[validators.required()])
    date_stop = DateField('End Date of Travel:',
                          format='%m/%d/%Y',
                          validators=[validators.required()])
    event_name = TextField('Event Name:', validators=[validators.required()])
    event_start = DateField('Event Start:',
                            format='%m/%d/%Y',
                            validators=[validators.required()])
    event_stop = DateField('Event Stop:',
                           format='%m/%d/%Y',
                           validators=[validators.required()])
    event_attendeetype = TextField('Attendee Type:',
                                   validators=[validators.required()])

    stsci_employee = SelectField('STScI Employee?',
                                 choices=[("yes", "yes"),
                                          ("no", "no")],
                                 validators=[validators.required()])
    external_organization = TextField('External Org.:')
    destination = TextField('Destination:',
                            validators=[validators.required()])
    wbs1 = IntegerField('WBS 1 (%):', validators=[validators.required()])
    wbs2 = IntegerField('WBS 2 (%):', default=int(0))
    wbs3 = IntegerField('WBS 3 (%):', default=int(0))
    purpose_of_travel = TextField('Purpose of Travel:',
                                  validators=[validators.required()])
    empl_org_num = SelectField('Employee Org #:',
                               choices=[("choice1", "choice1"),
                                        ("choice2", "choice2"),
                                        ("choice3", "choice3"),
                                        ("choice4", "choice4"),
                                        ("choice5", "choice5")],
                             validators=[validators.required()])
    travel_charges_org_num = SelectField('Travel charges Org #:',
                                       choices=[("choice1", "choice1"),
                                                ("choice2", "choice2"),
                                                ("choice3", "choice3"),
                                                ("choice4", "choice4"),
                                                ("choice5", "choice5")],
                                       validators=[validators.required()])

    need_advance = TextField('Do you need a travel advance?', validators=[validators.required()])
    how_much_advance = TextField('How much?')
    any_part_personal = TextField('Is any part of this trip personal?', validators=[validators.required()])
    personal_travel_dates = DateField('If so, specify dates:')
    personal_travel_destination = TextField('If so, specify destination:')

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






@app.route("/", methods=['GET', 'POST'])
def hello():
    form = BasicInfoForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        #    wbs_flag = True

        if form.validate():
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
            flash('List of potential problems:')
            flash('Required inputs not submitted')
            flash('Dates are not in mm/dd/yyyy format')
            if wbs_flag:
                flash('Sum of WBS values does not equal 100%')

    return render_template('travelreform.html', form=form)

"""
        name = request.form['name']
        title = request.form['title']
        phone = request.form['phone']
        email = request.form['email']
        date_start = request.form['date_start']
        date_stop = request.form['date_stop']
        event_name = request.form['event_name']
        event_start = request.form['event_start']
        event_stop = request.form['event_stop']
        event_attendeetype = request.form['event_attendeetype']
        stsci_employee = request.form['stsci_employee']
        external_organization = request.form['external_organization']
        destination = request.form['destination']
        wbs1 = request.form['wbs1']
        wbs2 = request.form['wbs2']
        wbs3 = request.form['wbs3']
        purpose_of_travel = request.form['purpose_of_travel']
        empl_org_num = request.form['empl_org_num']
        travel_charges_org_num = request.form['travel_charges_org_num']
        #if (int(wbs1) + int(wbs2) + int(wbs3)) != 100:
"""

if __name__ == "__main__":
    app.run()

