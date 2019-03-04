from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='Code and Coffee')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting minutes')