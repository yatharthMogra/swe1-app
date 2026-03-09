from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


class PollsSmokeTests(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text="Smoke test question?",
            pub_date=timezone.now(),
        )
        Choice.objects.create(question=self.question, choice_text="Choice A", votes=0)
        Choice.objects.create(question=self.question, choice_text="Choice B", votes=0)

    def test_root_redirects_to_polls(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/polls/")

    def test_polls_index_renders(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question.question_text)

    def test_polls_detail_renders(self):
        response = self.client.get(reverse("polls:detail", args=[self.question.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question.question_text)
