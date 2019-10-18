from django.core.mail import send_mail
from django.template import loader


def send_email(name,email,token):
    subject = '激活账户'
    message = '测试成功'
    context = {
        'name': name,
        'url': 'http://127.0.0.1:8000/axfuser/checkEmail/?token='+str(token)
    }
    html_message = loader.get_template('active.html').render(context=context)
    from_email = 'ccq1406159466@163.com'
    recipient_list = [email]

    send_mail(subject=subject, message=message, html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)
