from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse

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

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='Code Academy')
        self.assertEqual(str(meeting), resource.resourcetitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'event')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=se;f.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'pythonclubapp/index.html')