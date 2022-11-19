from django.conf import settings
from django.shortcuts import redirect
import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    """Осуществление заказа на checkout.stripe.com"""
    def get(self, request,  *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"

        # Нужно разобраться с Create Price
        # item_id = self.kwargs['item_id']
        # item = Item.objects.get(pk=item_id)

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1M5cwSKxvPpdM2FHaJmKgxMf',
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


class IndexPageView(ListView):
    """Главная страница."""
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'


class DetailPageView(TemplateView):
    """Отдельный товар."""
    template_name = 'item.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['item_id']
        item = Item.objects.get(pk=item_id)
        context = {
            'item': item,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        }
        return context
