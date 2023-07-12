from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from channel.models import Channel
from .models import Video


class VideoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test channel
        cls.channel = Channel.objects.create(name='Test Channel')

        # Create a test video
        video_file = SimpleUploadedFile(
            name='test_video.mp4',
            content=b'file_content',
            content_type='video/mp4'
        )
        cls.video = Video.objects.create(
            video=video_file,
            name='Test Video',
            description='Test Description',
            type='Test Type',
            channel_id=cls.channel
        )

    def test_video_name(self):
        video = Video.objects.get(id=self.video.id)
        expected_name = 'Test Video'
        self.assertEqual(video.name, expected_name)

    def test_video_description(self):
        video = Video.objects.get(id=self.video.id)
        expected_description = 'Test Description'
        self.assertEqual(video.description, expected_description)

    def test_video_channel(self):
        video = Video.objects.get(id=self.video.id)
        self.assertEqual(video.channel_id, self.channel)


