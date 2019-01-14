from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59
        )
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):

    def create_question(self, question_text, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(
            question_text=question_text,
            pub_date=time
        )

    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = self.create_question(
            question_text="Past question.",
            days=-30
        )
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], [
                '<Question: question_text: Past question.,pub_date: {day}>'
                .format(day=question.pub_date)
            ]
        )

    def test_future_question(self):
        self.create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_two_past_questions(self):
        first_past_question = self.create_question(
            question_text="Past question 1.",
            days=-30
        )
        second_past_question = self.create_question(
            question_text="Past question 2.",
            days=-5
        )
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], [
                '<Question: question_text: Past question 2.,pub_date: {day}>'
                .format(day=second_past_question.pub_date),
                '<Question: question_text: Past question 1.,pub_date: {day}>'
                .format(day=first_past_question.pub_date)
            ]
        )


class QuestionDetailViewTests(TestCase):

    def create_question(self, question_text, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(
            question_text=question_text,
            pub_date=time
        )

    def test_future_question(self):
        future_question = self.create_question(
            question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = self.create_question(
            question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
