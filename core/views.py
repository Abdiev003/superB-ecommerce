from django.shortcuts import render
from django.contrib.messages import success, error
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from core.models import Subscribe, Contact
from core.forms import SubscribeForm, ContactForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about_us.html')


class ContactView(CreateView):
    template_name = 'contact_us.html'
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('core:contact-us')

    def form_valid(self, form):
        success(
            self.request, 'We appreciate you contacting us/ [SuperB]. One of our colleagues will get back in touch with you soon!Have a great day!')
        return super().form_valid(form)


class SubscribeView(CreateView):
    template_name = 'index.html'
    model = Subscribe
    form_class = SubscribeForm

    def form_valid(self, form):
        success(
            self.request, 'Thank you for getting in touch! We appreciate you contacting us/ [SuperB].')
        return super().form_valid(form)

    def form_invalid(self, form):
        error(self.request, 'Something went wrong. Please try again.')
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")
