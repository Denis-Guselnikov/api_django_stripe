from django.contrib import admin
from django.urls import path
from products.views import CreateCheckoutSessionView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', TemplateView.as_view(template_name='cancel.html'), name='cancel'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('create-checkout-session', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', TemplateView.as_view(template_name='checkout.html'), name='checkout-page')
]
