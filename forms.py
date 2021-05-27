from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ComisionForm(FlaskForm):
    monto = FloatField(label='Monto', validators=[DataRequired(message='Introduzca una cantidad positiva porfavor'), NumberRange(min=0.01, message='Introduzca una cantidad positiva porfavor')])