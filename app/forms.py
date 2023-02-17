from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired()])
    email = StringField('E-Mail',validators=[InputRequired()])
    subject = StringField('Subject',validators=[InputRequired()])
    message= TextAreaField('Message', validators=[InputRequired()])
