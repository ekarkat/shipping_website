from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])

