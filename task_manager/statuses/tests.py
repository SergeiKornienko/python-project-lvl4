from django.test import TestCase, Client
from django.urls import reverse_lazy
from .models import Status


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

        status = Status.objects.get()
        response = self.client.post(
            reverse_lazy('update', kwargs={'pk': status.id}),
            data={'name': 'test2'},
        )
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertTrue(Status.objects.filter(name='test2'))

    def test_status_delete(self):
        status = Status.objects.get()
        response = self.client.post(
            reverse_lazy('delete', kwargs={'pk': status.id}),
        )
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertFalse(Status.objects.filter(name='test2'))
