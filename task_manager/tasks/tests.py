from django.test import TestCase, Client
from django.urls import reverse_lazy
from task_manager.tasks.models import Status, Task


class StatusTest(TestCase):
    fixtures = ['test.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='test', password='pass')
        self.response = self.client.post(
            reverse_lazy('create_status'),
            data={'name': 'test_status'},
        )

    def test_status_create(self):
        self.assertRedirects(self.response, reverse_lazy('statuses'))
        self.assertTrue(Status.objects.filter(name='test_status'))

    def test_status_update(self):
        status = Status.objects.get(name='test_status')
        response = self.client.post(
            reverse_lazy('update_status', kwargs={'pk': status.id}),
            data={'name': 'test2'},
        )
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertTrue(Status.objects.filter(name='test2'))

    def test_status_delete(self):
        status = Status.objects.get(name='test_status')
        response = self.client.post(
            reverse_lazy('delete_status', kwargs={'pk': status.id}),
        )
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertFalse(Status.objects.filter(name='test_status'))


class TaskTest(TestCase):
    fixtures = ['test.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='test', password='pass')
        self.response = self.client.post(
            reverse_lazy('create_task'),
            data={
                'name': 'test_task',
                'description': 'test',
                'status': 12,
                'performer': 16,
            },
        )

    def test_task_create(self):
        self.assertRedirects(self.response, reverse_lazy('tasks'))
        self.assertTrue(Task.objects.filter(name='test_task'))

    def test_task_update(self):
        task = Task.objects.get(name='test_task')
        response = self.client.post(
            reverse_lazy('update_task', kwargs={'pk': task.id}),
            data={
                'name': 'test_task2',
                'description': 'test2',
                'status': 10,
                'performer': 17,
            },
        )
        self.assertRedirects(response, reverse_lazy('tasks'))
        self.assertTrue(Task.objects.filter(description='test2'))

    def test_task_delete(self):
        task = Task.objects.get(name='test_task')
        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': task.id}),
        )
        self.assertRedirects(response, reverse_lazy('tasks'))
        self.assertFalse(Task.objects.filter(name='test_task'))
