from django.db import models

class Word(models.Model):
    word_text = models.CharField(max_length=100)  # 단어
    meaning = models.TextField()  # 단어의 의미
    pronunciation = models.CharField(max_length=100, blank=True, null=True)  # 발음 방법
    category = models.CharField(max_length=100, blank=True, null=True)  # 분류

    def __str__(self):
        return self.word_text
