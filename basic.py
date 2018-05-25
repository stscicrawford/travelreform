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
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = BasicInfoForm(request.form)

    print(form.errors)
    if request.method == 'POST':
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
        #    wbs_flag = True

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
            flash('Your title is ' + title)
            flash('Your phone number is ' + phone)

        else:
            flash('List of potential problems:')
            flash('Required inputs not submitted')
            flash('Dates are not in mm/dd/yyyy format')
            if wbs_flag:
                flash('Sum of WBS values does not equal 100%')

    return render_template('basic.html', form=form)

if __name__ == "__main__":
    app.run()

