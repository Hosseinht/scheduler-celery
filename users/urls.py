from django.urls import path

from .views import SignInView, SignUpView, sign_out, AccountView

app_name = "users"

urlpatterns = [
    path('', SignUpView.as_view(), name="home"),
    path('sign-in/', SignInView.as_view(), name="sign-in"),
    path('sign-out/', sign_out, name="sign-out"),
    path('account/', AccountView.as_view(), name="account"),
]
