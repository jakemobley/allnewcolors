from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user

class PostForm(FlaskForm):
	featured = SelectField('Featured?', choices=[
	                       ('no', 'no'), ('yes', 'yes')], default='no')
	edit_queue = SelectField('Add to Edit Queue?', choices=[
	                       ('no', 'no'), ('yes', 'yes')], default='no')
	markup_type = SelectField('Markup', choices=[('plaintext', 'Plain Text'), (
		'html', 'HTML')], default="plaintext")
	title = StringField('Title', validators=[DataRequired()])
	title_image = FileField('Choose Title Image', validators=[
            FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
	tags = SelectMultipleField('Tags (hold shift to select multiple)', choices=[('Career', 'Career'), 
		('Education', 'Education'), ('Finance', 'Finance'), ('Lifestyle', 'Lifestyle'), 
			('Wellness', 'Wellness')])
	description = StringField('Description', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')
