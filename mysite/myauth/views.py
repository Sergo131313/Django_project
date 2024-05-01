
"""
This Python script defines various views and functionality related to user authentication and password management.

Description:
    - It imports necessary modules and classes from Django.
    - It defines a RegisterView class based on CreateView to handle user registration.
        - It specifies the form_class, template_name, and success_url attributes.
        - It overrides the form_valid method to create a Profile object associated with the newly registered user and perform automatic login.
    - It defines a login_view function to handle user login.
    - It defines a logout_view function to handle user logout.
    - It defines a MyLogoutView class based on LogoutView to handle user logout with redirection.
    - It defines a change_password function to handle password change functionality.
    - It defines various views for password reset functionality.
    - Each view is associated with a specific template for rendering.

Note: This script provides functionality for user registration, login, logout, password change, and password reset. It utilizes Django's built-in authentication forms and views for managing user authentication and password-related tasks.

"""

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from .models import Profile
from django.shortcuts import render, get_object_or_404, redirect


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about_me')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user= self.object)
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password1')
        user = authenticate(self.request,username=username, password=password)
        login(request=self.request, user=user)
        return redirect("myauth:about_me")

    def login_view(request:HttpRequest) -> HttpResponse:
        if request.method == 'GET':
            if request.user.is_authenticated:
                return redirect('/admin/')
        return render(request, 'myauth/login.html')

        username = request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'myauth/login.html')



def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login"))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has changed succesfuly')
            return redirect('myauth:login')
    else:
        form= PasswordChangeForm(user=request.user)
    return render(request, 'myauth/change_password.html',{'form':form})


class AboutMeView(TemplateView):
    template_name = "myauth/about_me.html"


class ResetPasswordView(PasswordResetView):
    template_name = "myauth/password_reset_email.html"
    form_class = PasswordResetForm

    def get_success_url(self):
        return reverse_lazy('reset_password_done')



class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = "myauth/password_reset_done.html"


class PasswordResetConfirmViewCustom(PasswordResetConfirmView):
    template_name = "myauth/password_reset_form.html"
    success_url = ("password_reset_complete"),


class PasswordResetCompleteViewCustom(PasswordResetCompleteView):
    template_name = "myauth/password_reset_sent.html"