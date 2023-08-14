from rest_framework import routers
from rest_framework.routers import DefaultRouter

from api.polls.views import QuestionViewSet

router = routers.SimpleRouter()
router.register(r"questions", QuestionViewSet, basename="question")
urlpatterns = router.urls
