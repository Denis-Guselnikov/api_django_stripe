from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from django.http import JsonResponse

from django.views import View


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request,  *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        try:
            checkout_session = stripe.checkout.Session.create(            
                line_items=[
                    {                        
                        # 'price': '{{PRICE_ID}}',
                        'price': 'price_1M5QHyKxvPpdM2FH3KqZLVYF',                  
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + "/success",
                cancel_url=YOUR_DOMAIN + "/cancel",
            )

            return redirect(checkout_session.url, code=303)
        except Exception as e:
            return JsonResponse({'error': str(e)})
