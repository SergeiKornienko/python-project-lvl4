from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect

from task_manager.tasks import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy


class StatusesView(LoginRequiredMixin, ListView):
    model = models.Status
    queryset = models.Status.objects.all()
    template_name = 'statuses/statuses.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'statuses'


class CreateStatusView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Status
    form_class = forms.StatusForm
    template_name = 'statuses/create_status.html'
    success_url = reverse_lazy('statuses')
    success_message = gettext_lazy('Статус создан!')
    login_url = reverse_lazy('login')
    redirect_field_name = 'create_status'


class UpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = models.Status
    form_class = forms.StatusForm
    template_name = 'statuses/update_status.html'
    success_url = reverse_lazy('statuses')
    success_message = gettext_lazy('Статус изменен!')
    login_url = reverse_lazy('login')
    redirect_field_name = 'update_status'


class DeleteStatusView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = models.Status
    template_name = 'statuses/delete_status.html'
    success_url = reverse_lazy('statuses')
    login_url = reverse_lazy('login')
    redirect_field_name = 'delete_status'

    def get_success_url(self):
        messages.success(self.request, gettext_lazy('Статус удален!'))
        return self.success_url


class TaskView(LoginRequiredMixin, ListView):
    model = models.Task
    queryset = models.Task.objects.all()
    template_name = 'tasks/tasks.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'tasks'


class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('tasks')
    success_message = gettext_lazy('Задача создана!')
    login_url = reverse_lazy('login')
    redirect_field_name = 'create_task'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'tasks/update_task.html'
    success_url = reverse_lazy('tasks')
    success_message = gettext_lazy('Задача изменена!')
    login_url = reverse_lazy('login')
    redirect_field_name = 'update_task'


class DeleteTaskView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = models.Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks')
    login_url = reverse_lazy('login')
    redirect_field_name = 'delete_task'
    error_message = gettext_lazy(
        'Задачу может удалить только её автор.',
    )

    def dispatch(self, request, *args, **kwargs):
        if self.model.objects.get(
            pk=kwargs['pk']
        ).author_id != self.request.user.pk:
            messages.error(request, self.error_message)
            return HttpResponseRedirect('/tasks/')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, gettext_lazy('Задача удалена!'))
        return self.success_url
