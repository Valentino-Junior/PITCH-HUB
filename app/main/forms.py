from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField, SelectField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
    category = SelectField('Select category', choices=[('pickuppitch', 'Pick Up Lines'), ('techpitch', 'Technology'), ('businesspitch', 'Business'),('interviewpitch','Interview')])
    title = StringField('Title of your Pitch')
    description = TextAreaField('Type in your pitch')
    submit = SubmitField('Add Pitch')

class CommentForm(FlaskForm):
    description = TextAreaField('Add comment',validators=[Required()])
    submit = SubmitField()

class UpvoteForm(FlaskForm):
    submit = SubmitField()


class Downvote(FlaskForm):
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')