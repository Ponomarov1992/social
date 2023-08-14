from rest_framework import viewsets

from core.polls.models import Choice, Question

from . import serializers


class QuestionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = serializers.QuestionSerializer
    queryset = Question.objects.all()
