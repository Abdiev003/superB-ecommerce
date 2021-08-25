from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, TemplateView
from django.contrib.messages import success, error
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import redirect, render
from django.views.generic import CreateView, View, UpdateView

from accounts.forms import RegisterForm, LoginForm, UpdateProfile
from accounts.utils.tokens import account_activation_token
from accounts.utils.send_mail import send_confirmation_email

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('core:home')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        success(self.request, 'You were successfully login')
        return super().form_valid(form)

    def form_invalid(self, form):
        error(self.request, 'Sorry, that login was invalid. Please try again.')
        return super().form_invalid(form)


class RegisterCreateView(CreateView):
    model = User
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        site_adres = self.request.is_secure() and "https://" or "http://" + \
            self.request.META["HTTP_HOST"]  # https or http
        send_confirmation_email(user, site_adres)
        success(
            self.request, 'Please confirm your email address to complete the registration')
        return super().form_valid(form)


class UserActivate(View):
    def get(self, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            success(
                self.request, 'Thank you for your email confirmation. Now you can login your account.')
            return redirect(reverse_lazy('accounts:login'))
        else:
            error(self.request, 'Activation link is invalid!')
            return redirect(reverse_lazy('accounts:register'))


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class AccountInformationView(LoginRequiredMixin, UpdateView):
    template_name = 'account_information.html'
    form_class = UpdateProfile
    model = User

    def get_object(self, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('accounts:dashboard')
