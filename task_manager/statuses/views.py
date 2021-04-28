from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import StatusForm

from task_manager.statuses import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy


class StatusesView(ListView):
    model = models.Status
    queryset = models.Status.objects.all()
    template_name = 'statuses/statuses.html'


class CreateStatusView(SuccessMessageMixin, CreateView):
    model = models.Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = gettext_lazy('Статус создан!')


#
#
# class LoginUserView(SuccessMessageMixin, LoginView):
#     form_class = AuthenticationForm
#     template_name = 'users/login.html'
#     redirect_field_name = reverse_lazy('home')
#     success_message = gettext_lazy('Вы залогинены!')
#
#
# class LogoutUserView(SuccessMessageMixin, LogoutView):
#     model = User
#     template_name = 'home.html'
#     success_url = reverse_lazy('home')
#     info_message = gettext_lazy('Вы разлогинены!')
#
#     def dispatch(self, request, *args, **kwargs):
#         messages.info(request, self.info_message)
#         return super().dispatch(request, *args, **kwargs)
#
#
# class OwnerOnlyMixin:
#     model = User
#     success_url = reverse_lazy('users')
#     error_message = gettext_lazy(
#         'У вас нет прав для изменения другого пользователя.',
#     )
#
#     def dispatch(self, request, *args, **kwargs):
#         if kwargs['pk'] != self.request.user.pk:
#             messages.error(request, self.error_message)
#             return HttpResponseRedirect('/users/')
#         return super().dispatch(request, *args, **kwargs)
#

class UpdateUserView(
    LoginRequiredMixin, SuccessMessageMixin, UpdateView,
):
    model = models.Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = gettext_lazy('Статус изменен!')

#
#
# class DeleteUserView(
#     LoginRequiredMixin, OwnerOnlyMixin, SuccessMessageMixin, DeleteView,
# ):
#     model = User
#     template_name = 'users/delete.html'
#     success_url = reverse_lazy('home')
#     login_url = '/login/'
#
#     def get_success_url(self):
#         messages.success(self.request, gettext_lazy('Пользователь удален!'))
#         return self.success_url
