from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from accounts.views import (SignupView, SigninView, AccountSettingsView,
ForgotPasswordView, HomePageView)

# from django_messages.views import (inbox, outbox, trash, compose, reply, delete, undelete, view)
urlpatterns = patterns('',
    # user relates urls
    # url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^signup/', SignupView.as_view(), name='signup'),
    url(r'^signin/', SigninView.as_view(), name='signin'),
    url(r'^account/', login_required(AccountSettingsView.as_view()),
        name='account_settings'),
    url(r'^forgot-password/', ForgotPasswordView.as_view(),
        name='forgot_password'),
    url(r'^signout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='signout'),

    url((r'^$'), login_required(HomePageView.as_view()), name='home'),
    url(r'^home$', login_required(HomePageView.as_view()), name='home'),

    # (r'^home/', include('django_messages.urls')),
    # url(r'^messaging/', include('django_messages.urls')),
    # (r'^messaging/', include('django_messages.urls')),
)

