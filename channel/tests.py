from django.test import TestCase
from django.contrib.auth.models import User
from .models import Channel


class ChannelModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test channel
        cls.channel = Channel.objects.create(
            name='Test Channel',
            logo=None,
            background=None,
            description='Test Description',
            user_id=cls.user
        )

    def test_channel_name(self):
        channel = Channel.objects.get(id=self.channel.id)
        expected_name = 'Test Channel'
        self.assertEqual(channel.name, expected_name)

    def test_channel_description(self):
        channel = Channel.objects.get(id=self.channel.id)
        expected_description = 'Test Description'
        self.assertEqual(channel.description, expected_description)

    def test_channel_user(self):
        channel = Channel.objects.get(id=self.channel.id)
        self.assertEqual(channel.user_id, self.user)


