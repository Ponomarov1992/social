import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from core.polls import models

client = APIClient()


@pytest.mark.django_db
@pytest.fixture
def questions_fixture():
    questions = []
    for i in range(2):
        questions.append(models.Question.objects.create(question_text=f"Question #{i}"))
    return questions


@pytest.mark.django_db
class TestQuestionAPI:
    pytestmark = pytest.mark.django_db
    QUESTION_LIST_URL = reverse("question-list")
    DETAIL_QUESTION_URL = reverse("question-detail", args=[1])

    def test_list_questions(self, questions_fixture):
        resp = client.get(self.QUESTION_LIST_URL)

        assert resp.status_code == status.HTTP_200_OK
        data = resp.data
        first_question = data[0]
        assert len(data) == models.Question.objects.count()
        assert first_question["id"] == 1
        assert first_question["question_text"] == "Question #0"

    def test_detail_question(self, questions_fixture):
        resp = client.get(self.DETAIL_QUESTION_URL)

        assert resp.status_code == status.HTTP_200_OK
        question = models.Question.objects.get(pk=resp.data["id"])
        assert resp.data["id"] == question.pk
        assert resp.data["question_text"] == question.question_text
        assert "pub_date" in resp.data
        assert resp.data["pub_date"] is not None
