from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.sql.models import User
from flask import request



class EditProfileForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    about_me = TextAreaField('About me',validators=[Length(min=0,max=140)])
    submit = SubmitField('Submit')

    def __init__(self,original_username,*args,**kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)
        self.original_username = original_username
    
    def validate_username(self,username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError("Username already exists.")


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something',validators=[DataRequired(),Length(min=1,max=500)])
    submit = SubmitField('Post')


class SearchForm(FlaskForm):
    q = StringField("Search",validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm,self).__init__(*args,**kwargs)
