# # learn/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn.views import SubjectViewSet, ChapterViewSet, TopicViewSet, SubTopicViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'subtopics', SubTopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
