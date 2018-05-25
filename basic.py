from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField
from wtforms import validators, StringField, SubmitField, DateField


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class BasicInfoForm(Form):
    name = TextField('Name of Traveler:', validators=[validators.required()])
    title = TextField('Traveler Title:', validators=[validators.required()])
    phone = TextField('Phone:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])
    # data_start = DateField('Start Date', format='%m/%d/%Y')
    date_start = TextField('Start Date of Travel:',
                           validators=[validators.required()])
    date_stop = TextField('End Date of Travel:',
                          validators=[validators.required()])
    event_name = TextField('Event Name:', validators=[validators.required()])
    event_start = TextField('Event Start:', validators=[validators.required()])
    event_stop = TextField('Event Stop:', validators=[validators.required()])
    event_attendeetype = TextField('Attendee Type:',
                                   validators=[validators.required()])

    stsci_employee = TextField('STScI Employee (Y/N):',
                               validators=[validators.required()])
    external_organization = TextField('External Org.:',
                                      validators=[validators.required()])
    destination = TextField('Destination:',
                            validators=[validators.required()])
    wbs = TextField('WBS:', validators=[validators.required()])
    purpose_of_travel = TextField('Purpose of Travel:',
                                  validators=[validators.required()])
    empl_org_num = TextField('Employee Org #:',
                             validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = BasicInfoForm(request.form)
    empl_nums = ["1.1.01.00.76.03, FACO Facilities Operat",
                 "DO     Director's Office",
                 "1.1.01.20.10.40, ACS"]
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
        wbs = request.form['wbs']
        purpose_of_travel = request.form['purpose_of_travel']
        empl_org_num = request.form['empl_org_num']
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
            flash('Your title is ' + title)
            flash('Your phone number is ' + phone)

        else:
            flash('All the form fields are required. ')
 
    return render_template('webform.html', form=form, empl_nums=empl_nums)
 
if __name__ == "__main__":
    app.run()
