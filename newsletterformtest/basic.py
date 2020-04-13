from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, 
                    SelectField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app= Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    first_name = StringField("What's your  name?", validators=[DataRequired()])
    email_address = TextAreaField()
    user_type = SelectField(u'What describes you best?', 
                choices= [('beg', 'Beginner PM'), ('adv', 'Advanced PM'), ('start', 'Startup Founder'), ('stu', 'Student'), ('oth', 'Other')])
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['first_name'] = form.first_name.data
        session['email_address']  = form.email_address.data
        session['user_type'] = form.user_type.data

        return redirect(url_for('thankyou'))

    return render_template('hello.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)





