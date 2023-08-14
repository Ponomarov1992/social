from rest_framework.serializers import ModelSerializer

from core.polls.models import Choice, Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date")


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "question", "choice_text", "votes")
