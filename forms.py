from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Имя', validators=[
        DataRequired(message='Пожалуйста, введите ваше имя'),
        Length(min=2, max=50, message='Имя должно содержать от 2 до 50 символов')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Пожалуйста, введите ваш email'),
        Email(message='Пожалуйста, введите корректный email адрес')
    ])
    phone = StringField('Телефон', validators=[
        DataRequired(message='Пожалуйста, введите ваш телефон'),
        Length(min=10, max=20, message='Телефон должен содержать от 10 до 20 символов')
    ])
    message = TextAreaField('Сообщение', validators=[
        Length(max=500, message='Сообщение не должно превышать 500 символов')
    ])
