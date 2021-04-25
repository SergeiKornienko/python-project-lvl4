from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'


class UsersView(ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'tasks/users.html'


class RegisterUserView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('login')
    success_message = gettext_lazy('Вы зарегистрированы!')


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'tasks/login.html'
    redirect_field_name = reverse_lazy('home')
    success_message = gettext_lazy('Вы залогинены!')


class LogoutUserView(SuccessMessageMixin, LogoutView):
    model = User
    template_name = 'home.html'
    success_url = reverse_lazy('home')
    info_message = gettext_lazy('Вы разлогинены!')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.info_message)
        return super().dispatch(request, *args, **kwargs)


class OwnerOnlyMixin:
    model = User
    success_url = reverse_lazy('users')
    error_message = gettext_lazy(
        'У вас нет прав для изменения другого пользователя.',
    )

    def dispatch(self, request, *args, **kwargs):
        if kwargs['pk'] != self.request.user.pk:
            messages.error(request, self.error_message)
            return HttpResponseRedirect('/users/')
        return super().dispatch(request, *args, **kwargs)


class UpdateUserView(
    LoginRequiredMixin, OwnerOnlyMixin, SuccessMessageMixin, UpdateView,
):
    model = User
    form_class = RegistrationForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('home')
    success_message = gettext_lazy('Данные изменены!')
    login_url = '/login/'


class DeleteUserView(
    LoginRequiredMixin, OwnerOnlyMixin, SuccessMessageMixin, DeleteView,
):
    model = User
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('home')
    login_url = '/login/'

    def get_success_url(self):
        messages.success(self.request, gettext_lazy('Пользователь удален!'))
        return self.success_url
