from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from accounts.views import (
    CustomLoginView,
    RegisterCreateView,
    UserActivate,
    DashboardView,
    AccountInformationView,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('account-information/', AccountInformationView.as_view(), name='account-information'),

    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
            UserActivate.as_view(), name='activate'),
]
