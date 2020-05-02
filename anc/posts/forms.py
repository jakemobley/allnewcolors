from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class PostForm(FlaskForm):
	markup_type = SelectField('Markup', choices=[('plaintext', 'Plain Text'), (
		'html', 'HTML')], default="plaintext")
	title = StringField('Title', validators=[DataRequired()])
	title_image = FileField('Choose Title Image', validators=[
            FileAllowed(['jpg', 'jpeg', 'png', 'gif']), FileRequired()])
	description = StringField('Description', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')
