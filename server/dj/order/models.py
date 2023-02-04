from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

import uuid
import json

from yookassa import Configuration, Payment


Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID 
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY


class Order(models.Model):

    name = models.CharField(max_length=255)

    user = models.ForeignKey(User, related_name='user_orders', on_delete=models.CASCADE)

    product_id = models.CharField(max_length=100, blank=True, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)

    payment_url = models.TextField(blank=True, null=True)
    payment_id = models.TextField(blank=True, null=True)
    payment_status = models.TextField(blank=True, null=True)

    randomID = models.CharField(max_length=100, blank=True, null=False)


    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.name

    def get_payment_url(self):
        if self.payment_url:

            return self.payment_url
            
        elif self.product_id:

            self.payment_url = self.make_payment_url()
            self.save()

            return self.payment_status
    
        else:
            return ''

    def get_payment_status(self):
        if self.payment_status == 'succeeded' or self.payment_status == 'canceled':

            return self.payment_status
            
        elif self.payment_status != 'succeeded':

            self.payment_status = self.make_payment_status()
            self.save()

            return self.payment_status
    
    def make_payment_url(self):

        payment = Payment.create({
        "amount": {
            "value": f"{self.paid_amount}",
        "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://www.example.com/return_url"
        },
        "capture": True,
        "description": "Приобретение видеоурока"

        }, uuid.uuid4())

        payment_data = json.loads(payment.json())
        payment_id = payment_data['id']
        payment_url = (payment_data['confirmation'])['confirmation_url']

        payment = json.loads((Payment.find_one(payment_id)).json())

        print(payment_data)

        self.payment_id = payment_id
        self.save()

        return payment_url


    def make_payment_status(self):

        payment = json.loads((Payment.find_one(self.payment_id)).json()) 

        return payment['status']