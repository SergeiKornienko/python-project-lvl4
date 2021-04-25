from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class UserTest(TestCase):
    # fixtures = ['user']

    def setUp(self):
        self.client = Client()
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

    def test_user_create(self):
        self.assertRedirects(self.response, reverse_lazy('login'))
        self.assertTrue(
            User.objects.filter(
                username='first', first_name='name', last_name='surname',
            ),
        )

    def test_user_update(self):
        self.client.login(username='first', password='pass')
        user = User.objects.get()
        response = self.client.post(
            reverse_lazy('update', kwargs={'pk': user.id}),
            data={
                'username': 'first',
                'first_name': 'name123',
                'last_name': 'surname+',
                'password1': 'pass',
                'password2': 'pass',
            },
        )
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertTrue(
            User.objects.filter(
                username='first', first_name='name123', last_name='surname+',
            ),
        )

    def test_user_delete(self):
        self.client.login(username='first', password='pass')
        user = User.objects.get()
        response = self.client.post(
            reverse_lazy('delete', kwargs={'pk': user.id}),
        )
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertFalse(
            User.objects.filter(
                username='first', first_name='name123', last_name='surname+',
            ),
        )
