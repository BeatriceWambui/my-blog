from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,TextAreaField,RadioField
from wtforms.validators import Required
from wtforms import ValidationError

class PostForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    description = TextAreaField('please share a post',validators=[Required()])
    category = TextAreaField('Label', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment')
    submit = SubmitField('Submit')

