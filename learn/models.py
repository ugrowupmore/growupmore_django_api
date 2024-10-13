# learn/models.py

from django.db import models
from django.utils.text import slugify
from utils.enums import StatusType
from utils.soft_delete import SoftDeleteModel
from utils.image_size import validate_image_size_2mb

# Subject Model
class Subject(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='NA')
    subject_code = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(
        upload_to='subjects_images/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    yt_thumbnail_image = models.ImageField(
        upload_to='subjects_yt_thumbnails/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    alt_text = models.TextField(default='NA')
    short_intro = models.TextField(default='NA')
    long_intro = models.TextField(default='NA')
    video_url = models.TextField(default='NA')
    video_title = models.TextField(default='NA')
    video_description = models.TextField(default='NA')
    prerequisites = models.TextField(default='NA')
    tags = models.JSONField(default=list, blank=True)
    status = models.CharField(
        max_length=10,
        choices=StatusType.choices,
        default=StatusType.DRAFT
    )
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    average_review = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    class Meta:
        db_table = '"learn"."subjects"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['subject_code']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):
        # Generate slug if not already set
        if not self.slug and self.name:
            self.slug = slugify(self.name.lower().replace(' ', '_'))
        super(Subject, self).save(*args, **kwargs)

        # Cascade is_active and is_deleted to related Chapters, Topics, and SubTopics
        if not self.is_active:
            Chapter.objects.filter(subject=self).update(is_active=False)
            Topic.objects.filter(subject=self).update(is_active=False)
            SubTopic.objects.filter(subject=self).update(is_active=False)

        if self.is_deleted:
            Chapter.objects.filter(subject=self).update(is_deleted=True)
            Topic.objects.filter(subject=self).update(is_deleted=True)
            SubTopic.objects.filter(subject=self).update(is_deleted=True)


# Chapter Model
class Chapter(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(
        Subject,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='chapters'
    )
    name = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(
        upload_to='chapters_images/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    yt_thumbnail_image = models.ImageField(
        upload_to='chapters_yt_thumbnails/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    short_intro = models.TextField(default='NA')
    long_intro = models.TextField(default='NA')
    video_url = models.TextField(default='NA')
    video_title = models.TextField(default='NA')
    video_description = models.TextField(default='NA')
    prerequisites = models.TextField(default='NA')
    tags = models.JSONField(default=list, blank=True)
    display_order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10,
        choices=StatusType.choices,
        default=StatusType.DRAFT
    )
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    average_review = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    class Meta:
        db_table = '"learn"."chapters"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['subject']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):
        # Generate slug using subject code + chapter name
        if not self.slug and self.name and self.subject:
            subject_code = self.subject.subject_code if self.subject else 'NA'
            self.slug = slugify(f"{subject_code}-{self.name}".lower().replace(' ', '_'))
        super(Chapter, self).save(*args, **kwargs)

        # Ensure subject is_active and is_deleted status align with chapter
        if self.is_active and self.subject and not self.subject.is_active:
            self.subject.is_active = True
            self.subject.save()

        if not self.is_deleted and self.subject and self.subject.is_deleted:
            self.subject.is_deleted = False
            self.subject.save()

        # Cascade is_active and is_deleted to related Topics and SubTopics
        if not self.is_active:
            Topic.objects.filter(chapter=self).update(is_active=False)
            SubTopic.objects.filter(chapter=self).update(is_active=False)

        if self.is_deleted:
            Topic.objects.filter(chapter=self).update(is_deleted=True)
            SubTopic.objects.filter(chapter=self).update(is_deleted=True)


# Topic Model
class Topic(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(
        Subject,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='topics'
    )
    chapter = models.ForeignKey(
        Chapter,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='topics'
    )
    title = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(
        upload_to='topics_images/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    yt_thumbnail_image = models.ImageField(
        upload_to='topics_yt_thumbnails/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    short_intro = models.TextField(default='NA')
    long_intro = models.TextField(default='NA')
    video_url = models.TextField(default='NA')
    video_title = models.TextField(default='NA')
    video_description = models.TextField(default='NA')
    tags = models.JSONField(default=list, blank=True)
    status = models.CharField(
        max_length=10,
        choices=StatusType.choices,
        default=StatusType.DRAFT
    )
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    average_review = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    class Meta:
        db_table = '"learn"."topics"'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['subject']),
            models.Index(fields=['chapter']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):
        # Generate slug using subject id + chapter id + topic title
        if not self.slug and self.title and self.subject and self.chapter:
            self.slug = slugify(f"{self.subject.id}-{self.chapter.id}-{self.title}".lower().replace(' ', '_'))
        super(Topic, self).save(*args, **kwargs)

        # Ensure subject and chapter are_active and is_deleted status align with topic
        if self.is_active:
            if self.chapter and not self.chapter.is_active:
                self.chapter.is_active = True
                self.chapter.save()
            if self.subject and not self.subject.is_active:
                self.subject.is_active = True
                self.subject.save()

        if not self.is_deleted:
            if self.chapter and self.chapter.is_deleted:
                self.chapter.is_deleted = False
                self.chapter.save()
            if self.subject and self.subject.is_deleted:
                self.subject.is_deleted = False
                self.subject.save()

        # Cascade is_active and is_deleted to related SubTopics
        if not self.is_active:
            SubTopic.objects.filter(topic=self).update(is_active=False)

        if self.is_deleted:
            SubTopic.objects.filter(topic=self).update(is_deleted=True)


# Sub Topic Model
class SubTopic(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(
        Subject,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subtopics'
    )
    chapter = models.ForeignKey(
        Chapter,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subtopics'
    )
    topic = models.ForeignKey(
        Topic,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subtopics'
    )
    title = models.TextField(default='NA')
    description = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(
        upload_to='subtopics_images/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    yt_thumbnail_image = models.ImageField(
        upload_to='subtopics_yt_thumbnails/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    short_intro = models.TextField(default='NA')
    long_intro = models.TextField(default='NA')
    video = models.FileField(
        upload_to='subtopics_videos/',
        max_length=200,
        null=True,
        blank=True,
        validators=[validate_image_size_2mb]
    )
    video_title = models.TextField(default='NA')
    video_description = models.TextField(default='NA')
    tags = models.JSONField(default=list, blank=True)
    status = models.CharField(
        max_length=10,
        choices=StatusType.choices,
        default=StatusType.DRAFT
    )
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = '"learn"."sub_topics"'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['subject']),
            models.Index(fields=['chapter']),
            models.Index(fields=['topic']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):
        # Generate slug using subject id + chapter id + topic id + subtopic title
        if not self.slug and self.title and self.subject and self.chapter and self.topic:
            self.slug = slugify(f"{self.subject.id}-{self.chapter.id}-{self.topic.id}-{self.title}".lower().replace(' ', '_'))
        super(SubTopic, self).save(*args, **kwargs)

        # Ensure subject, chapter, and topic are_active and is_deleted status align with subtopic
        if self.is_active:
            if self.topic and not self.topic.is_active:
                self.topic.is_active = True
                self.topic.save()
            if self.chapter and not self.chapter.is_active:
                self.chapter.is_active = True
                self.chapter.save()
            if self.subject and not self.subject.is_active:
                self.subject.is_active = True
                self.subject.save()

        if not self.is_deleted:
            if self.topic and self.topic.is_deleted:
                self.topic.is_deleted = False
                self.topic.save()
            if self.chapter and self.chapter.is_deleted:
                self.chapter.is_deleted = False
                self.chapter.save()
            if self.subject and self.subject.is_deleted:
                self.subject.is_deleted = False
                self.subject.save()
