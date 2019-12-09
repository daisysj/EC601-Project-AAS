from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

class DataForm(FlaskForm):
    GRE = StringField('GRE Score(0-340)',validators=[DataRequired()])
    TOEFL = StringField('TOEFl Score(0-120)', validators=[DataRequired()])
    rating = StringField('University Rating', validators=[DataRequired()])
    SOP = StringField('Statement of Purpose(0-5)', validators=[DataRequired()])
    LOR = StringField('Letter of Recommendation(0-5)', validators=[DataRequired()])
    CGPA = StringField('Cumulative GPA(0-4)', validators=[DataRequired()])
    Research = StringField('Research(0/1)', validators=[DataRequired()])
    submit = SubmitField('Submit')