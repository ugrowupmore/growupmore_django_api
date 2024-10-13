from rest_framework import serializers
from learn.models import Subject, Chapter, Topic, SubTopic

class SubjectSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    chapter_name = serializers.CharField(source='chapter.name', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'

class SubTopicSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    chapter_name = serializers.CharField(source='chapter.name', read_only=True)
    topic_title = serializers.CharField(source='topic.title', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = SubTopic
        fields = '__all__'
