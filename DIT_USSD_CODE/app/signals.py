from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from .sms import SendSMS
from . import Scapper, ussd

@receiver(post_save, sender='app.UserSelection')
def extracting_comment(sender, **kwargs):
    student =kwargs['instance'].student
    result_type = kwargs['instance'].value
    print('start opening chrome')
    if result_type == 0:
        print('ok')
        status = ussd.checking_registration(email=student.email, password=student.password)
        sms_obj = SendSMS()
        sms_obj.sending(student.phone_number, status)

    else:
        results = Scapper.extractingResults(result_type=result_type, username=student.email, password=student.password)
        sms_obj = SendSMS()
        sms_obj.sending(student.phone_number, results)
    