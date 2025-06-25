import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_contact_email(phone, names):
    """Отправка заявки на электронную почту"""
    
    # Настройки для Gmail SMTP (можно изменить для других провайдеров)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    # Email настройки (нужно будет задать через переменные окружения)
    sender_email = os.environ.get('SENDER_EMAIL', 'your-email@gmail.com')
    sender_password = os.environ.get('SENDER_PASSWORD', '')
    recipient_email = os.environ.get('RECIPIENT_EMAIL', 'your-email@gmail.com')
    
    # Создание сообщения
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Новая заявка с сайта молебнов"
    
    # Тело письма
    body = f"""
Новая заявка с сайта:

Телефон: {phone}
Имена для молебна: {names}
Время подачи: {datetime.now().strftime('%d.%m.%Y %H:%M')}

---
Автоматическое уведомление с сайта молебнов
"""
    
    message.attach(MIMEText(body, "plain", "utf-8"))
    
    try:
        # Подключение к серверу и отправка
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Ошибка отправки письма: {e}")
        return False

def send_simple_email(phone, names):
    """Упрощенная версия для локального тестирования"""
    try:
        # Логирование заявки в файл
        with open('contact_requests.log', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()}: Телефон: {phone}, Имена: {names}\n")
        
        print(f"Новая заявка: {phone} - {names}")
        return True
    except Exception as e:
        print(f"Ошибка сохранения заявки: {e}")
        return False