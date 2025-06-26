import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import DataRequired, Email, Length
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "wellness-landing-secret-key")

EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")

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

        # Отримуємо дані з форми
        phone = form.phone.data
        names = form.names.data

        # Формуємо повідомлення
        subject = "Новая молитвенная записка с сайта"
        body = f"Телефон: {phone}\nИмена: {names}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = Email
        msg['To'] = "maks4ssd@gmail.com"

        try:
            server = smtplib.SMTP_SSL("smtp.ukr.net", 465)
            server.login(EMAIL, PASSWORD)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            server.quit()
            flash('Спасибо за ваше обращение! Мы свяжемся с вами в ближайшее время.', 'success')
        except Exception as e:
            flash(f'Ошибка при отправке письма: {str(e)}', 'danger')

        
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
