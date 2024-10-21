from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from learn.filters import SubjectFilter, ChapterFilter, TopicFilter, SubTopicFilter
from utils.pagination import StandardResultsSetPagination
from learn.models import Subject, Chapter, Topic, SubTopic
from learn.serializers import SubjectSerializer, ChapterSerializer, TopicSerializer, SubTopicSerializer
from utils.views import SoftDeleteViewSet

class SubjectViewSet(SoftDeleteViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  
    filterset_class = SubjectFilter  
    search_fields = ['name', 'subject_code', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'name', 'subject_code', 'status', 'is_active', 'is_deleted']
    lookup_field = 'id'
    pagination_class = StandardResultsSetPagination

class ChapterViewSet(SoftDeleteViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ChapterFilter
    search_fields = ['name', 'subject__name', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'name', 'subject__name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'id'
    pagination_class = StandardResultsSetPagination

class TopicViewSet(SoftDeleteViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TopicFilter
    search_fields = ['title', 'chapter__name', 'subject__name', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'title', 'chapter__name', 'subject__name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'id'
    pagination_class = StandardResultsSetPagination

class SubTopicViewSet(SoftDeleteViewSet):
    queryset = SubTopic.objects.all()
    serializer_class = SubTopicSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = SubTopicFilter
    search_fields = ['title', 'topic__title', 'chapter__name', 'subject__name', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'title', 'topic__title', 'chapter__name', 'subject__name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'id'
    pagination_class = StandardResultsSetPagination
