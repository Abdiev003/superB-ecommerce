from django.urls import path

from core.views import (
    index,
    about,
    ContactView,
    SubscribeView,
    FAQView,
)

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('about-us/', about, name='about-us'),
    path('contact-us/', ContactView.as_view(), name='contact-us'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('faq/', FAQView.as_view(), name='faq-help'),
]