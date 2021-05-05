from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# from django.http import HttpResponseRedirect
from .forms import StatusForm

from task_manager.tasks import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy


class StatusesView(LoginRequiredMixin, ListView):
    model = models.Status
    queryset = models.Status.objects.all()
    template_name = 'tasks/statuses/statuses.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'statuses'


class CreateStatusView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Status
    form_class = StatusForm
    template_name = 'tasks/statuses/create_status.html'
    success_url = reverse_lazy('statuses')
    success_message = gettext_lazy('Статус создан!')
    login_url = reverse_lazy('login')
    redirect_field_name = 'create_status'


class UpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = models.Status
    form_class = StatusForm
    template_name = 'tasks/statuses/update_status.html'
    success_url = reverse_lazy('statuses')
    success_message = gettext_lazy('Статус изменен!')
    login_url = reverse_lazy('login')
    redirect_field_name = 'update_status'


class DeleteStatusView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = models.Status
    template_name = 'tasks/statuses/delete_status.html'
    success_url = reverse_lazy('statuses')
    login_url = reverse_lazy('login')
    redirect_field_name = 'delete_status'

    def get_success_url(self):
        messages.success(self.request, gettext_lazy('Статус удален!'))
        return self.success_url
