from django.urls import path
from django.views.generic import TemplateView

from .views import IndexPageView, DetailPageView, CreateCheckoutSessionView


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('item/<int:item_id>/', DetailPageView.as_view(), name='item'),
    path('buy/<int:item_id>/', CreateCheckoutSessionView.as_view(),
         name='buy'),
    path('cancel/', TemplateView.as_view(template_name='cancel.html'),
         name='cancel'),
    path('success/', TemplateView.as_view(template_name='success.html'),
         name='success'),
]
