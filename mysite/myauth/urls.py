
"""
This Django URL configuration defines URL patterns for user authentication and password-related views.

Description:
    - It imports necessary modules and classes from Django.
    - It imports views from the current app and Django's built-in authentication views.
    - It specifies an app name for URL namespaces.
    - It defines URL patterns using the path() function.
    - Each URL pattern is associated with a corresponding view.
    - Views such as LoginView, RegisterView, logout_view, change_password, and AboutMeView are used for user authentication and profile management.
    - Password-related views such as PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, and PasswordResetCompleteView are also defined.

Note: This URL configuration provides endpoints for user login, registration, logout, password change, password reset, and profile management.

"""

from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import path

from .views import RegisterView, logout_view, change_password, AboutMeView
from django.contrib.auth import views as auth_views

app_name = 'myauth'

urlpatterns = [
    path("login/",
         LoginView.as_view(
             template_name="myauth/login.html",
             redirect_authenticated_user=True
         ),
         name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',logout_view,name='logout'),
    path('changepassword/',change_password,name='changePassword'),
    path("profile/", AboutMeView.as_view(), name='profile'),
    path('reset_password/',PasswordResetView.as_view(),name='reset_password'),
    path('reset_password/done/',PasswordResetDoneView.as_view(),name='reset_password_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    ]