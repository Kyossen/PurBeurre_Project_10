#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This import is obligatory for the good of the system
This below, the some urls of the platform for users app"""

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^connect.html', views.connect, name="connect"),
    url(r'^sign_up.html', views.sign_up, name="sign_up"),
    # url(r'^forgot_password.html', views.forgot_password, name="forgot_password"),
    # url(r'^reset_password.html', views.reset_password, name="reset_password"),
    url(r'^dashboard.html', views.dashboard, name="dashboard"),
    url(r'^disconnect.html', views.disconnect, name="disconnect"),

    #  Password reset URL
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name="password_reset"),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]