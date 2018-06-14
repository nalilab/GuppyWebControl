from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, IntegerField, FloatField, HiddenField
from wtforms.validators import DataRequired, ValidationError, NumberRange

class UpdateForm(FlaskForm):
    '''
    The form for connecting to the Arduino
    '''
    id = HiddenField('A hidden field');
    serial_port = StringField('Update to port:', validators=[DataRequired()])
    submit = SubmitField('Update port')

class DisconnectForm(FlaskForm):
    '''
    The form for disconnecting from the Arduino
    '''
    id = HiddenField('A hidden field');
    submit = SubmitField('Disconnect')

class ConnectForm(FlaskForm):
    '''
    The form for connecting to the camera
    '''
    id = HiddenField('A hidden field');
    folder = StringField('Folder name:', validators=[DataRequired()], description = 'Folder to watch')
    name = StringField('Name of the Camera:', description = 'Name', default = 'Oven')
    submit = SubmitField('Connect')

class ReConnectForm(FlaskForm):
    '''
    The form for recconnecting to the Arduino
    '''
    id = HiddenField('A hidden field');
    submit = SubmitField('Connect')
