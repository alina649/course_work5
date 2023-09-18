from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from users.apps import UsersConfig
from .views import RegisterView, UserUpdateView, confirm_email, activate_email, password_reset

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),

    path('confirm', confirm_email, name='confirm'),
    path('activate<str:key>', activate_email, name='activate'),
    path('password_reset/', password_reset, name='password_reset'),

]