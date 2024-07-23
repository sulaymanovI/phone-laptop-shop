from django.urls import path
from .views import *
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView)

urlpatterns = [
    path('sign-up/' , SignUpAPIView.as_view()),
    path('login/' , LoginView.as_view()),
    path('logout/' , LogoutView.as_view()),
    path('password-reset/' , PasswordResetView.as_view(template_name='password-reset.html'),name='password_reset'),
    path('password-reset-done/' , PasswordResetDoneView.as_view(template_name='password-reset-done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/' , PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/' , PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'),name='password_reset_complete'),
]
