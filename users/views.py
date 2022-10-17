from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth import logout, login, authenticate

from .decorators import login_forbidden
from .forms import (
    UserForm,
    AuthForm,
)


class SignUpView(generic.FormView):
    template_name = "users/sign_up.html"
    form_class = UserForm
    success_url = "/account/"

    def form_valid(self, form):
        obj = form.save()
        login(self.request, obj)
        return super().form_valid(form)

    @method_decorator(login_forbidden)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SignInView(generic.FormView):
    template_name = "users/sign_in.html"
    form_class = AuthForm
    success_url = "/account/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return super(SignInView, self).form_valid(form)
        else:
            return self.form_invalid(form)

    @method_decorator(login_forbidden)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def sign_out(request):
    logout(request)
    return redirect(reverse('users:sign-in'))


class AccountView(generic.TemplateView):
    template_name = "users/account.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
