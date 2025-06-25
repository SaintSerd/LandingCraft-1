import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import DataRequired, Email, Length

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "wellness-landing-secret-key")

class ContactForm(FlaskForm):
    phone = StringField('Номер телефона', validators=[
        DataRequired(message='Пожалуйста, введите ваш телефон'),
        Length(min=10, max=20, message='Телефон должен содержать от 10 до 20 символов')
    ])
    names = StringField('5 имён через запятую', validators=[
        DataRequired(message='Пожалуйста, введите 5 имён через запятую'),
        Length(min=5, max=200, message='Введите от 5 до 200 символов')
    ])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    
    if form.validate_on_submit():
        # In a real application, you would process the form data here
        # For example, send an email, save to database, etc.
        flash('Спасибо за ваше обращение! Мы свяжемся с вами в ближайшее время.', 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
