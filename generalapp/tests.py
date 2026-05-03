from django.test import TestCase
from generalapp.mailservice import send_mail

# Create your tests here.

send_mail("uzomamicheal07@gmail.com", "<p>hello email is working</p>", "test mail", "micheal")
