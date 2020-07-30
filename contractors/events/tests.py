from django.test import TestCase
from .models import Event

class EventTestCase(TestCase):
    def setUp(self):
        event = Event.objects.create(
            name="ET 1",
            total_fee_no_gst=1000,
            )

    def test_Events_can_speak(self):
        """Events financial calculations done correctly"""
        event = Event.objects.get(name="ET 1")
        self.assertEqual(event.calculate_gst(), 100)
