from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.conf import settings
from users.forms import UserRegisterForm, UserProfileForm, ManagerUpdateForm
from users.models import User

from users.utils import confirm_user_email, create_secret_key


class RegisterView(CreateView):
    """ Регистрация нового пользователя и отправка подтверждения на email пользователя """
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserManagerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование Менеджером статуса пользователя """
    model = User
    form_class = ManagerUpdateForm
    success_url = reverse_lazy('users:user_list')
    permission_required = 'users.block_another_user'


class UserListView(ListView):
    model = User


class UsersDetailView(DetailView):
    model = User
    template_name = "users/users_detail.html"


class UserUpdateView(UpdateView):
    """Профиль пользователя """
    model = User
    success_url = reverse_lazy("users:profile")
    form_class = UserProfileForm
    template_name = "users/user_detail.html"

    def get_object(self, queryset=None):
        return self.request.user


def confirm_email(request):
    """подтверждаем почту"""
    confirm_user_email(request, request.user)
    return redirect(reverse('users:profile'))


def activate_email(request, key):
    """активируем почту"""
    print(request.user.email_key, key, sep='\n')
    if request.user.email_key == key:
        request.user.email_confirmed = True
        request.user.email_key = None
        request.user.save()

    else:
        print('Ключ не актуален')
        print(request.user.email_key, key, sep='\n')
    return redirect('/')


def password_reset(request):
    """генерируем пароль для неавторизованного пользователя"""
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = create_secret_key(12)
            user.set_password(new_password)
            user.save()
            login(request, user)

            send_mail(
                subject='Вы запросили смену пароля',
                message=f'Ваш новый пароль: {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email]
            )

            return redirect(reverse("users:login"))  # все ок -> логин
        # не ок -> Error message + остаемся тут же
        except User.DoesNotExist:
            return render(request, 'users/password_reset_form.html',
                          {'error_message': 'Такого пользователя не существует'})
    return render(request, 'users/password_reset_form.html')


from django.shortcuts import render

# Create your views here.
