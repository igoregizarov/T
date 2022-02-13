from django.db import models

# Create your models here.

from django.db import models
from authapp.models import PollingUser


class QuestionsCategory(models.Model):
    name = models.CharField(max_length=4096, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Questions(models.Model):
    name = models.CharField(max_length=4096, unique=True)
    questions_category_id = models.ForeignKey(QuestionsCategory, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.questions_category_id.name})'


class Answer(models.Model):
    name = models.CharField(max_length=4096, blank=True)
    questions_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name


class ChoiseVoit(models.Model):
    name = models.CharField(max_length=4096)
    user = models.ForeignKey(PollingUser, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    questions_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ChoisePoll(models.Model):
    name = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(PollingUser, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    questions_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name