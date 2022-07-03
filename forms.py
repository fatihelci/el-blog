from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, EqualTo, Length
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    email = StringField("Your Email", validators=[DataRequired(), Email()])
    password = PasswordField("Your Password", validators=[DataRequired(), EqualTo("password_confirm", message="Passwords must match"), Length(min=6, max=10, message="Min 6 Max 10 chars.")])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=10)])
    submit = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    email = StringField("Your Email", validators=[DataRequired(), Email()])
    password = PasswordField("Your Password", validators=[DataRequired()])
    submit = SubmitField("LET ME IN!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("send comment!")
