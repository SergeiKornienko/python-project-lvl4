from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class UserTest(TestCase):
    fixtures = ['test.json']

    def setUp(self):
        self.client = Client()

    def test_user_create(self):
        self.response = self.client.post(
            reverse_lazy('register'),
            data={
                'username': 'first',
                'first_name': 'name',
                'last_name': 'surname',
                'password1': 'pass',
                'password2': 'pass',
            },
        )
        self.assertRedirects(self.response, reverse_lazy('login'))
        self.assertTrue(
            User.objects.filter(
                username='first', first_name='name', last_name='surname',
            ),
        )

    def test_user_update(self):
        self.client.login(username='test', password='pass')
        user = User.objects.get(username='test')
        response = self.client.post(
            reverse_lazy('update_user', kwargs={'pk': user.id}),
            data={
                'username': 'test1',
                'first_name': 'name1',
                'last_name': 'surname+',
                'password1': 'pass',
                'password2': 'pass',
            },
        )
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertTrue(
            User.objects.filter(
                username='test1', first_name='name1', last_name='surname+',
            ),
        )

    def test_user_delete(self):
        self.client.login(username='test', password='pass')
        user = User.objects.get(username='test')
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': user.id}),
        )
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertFalse(
            User.objects.filter(
                username='test', first_name='test', last_name='test',
            ),
        )
