from django.db import models

class Word(models.Model):
    word_text = models.CharField(max_length=100)  # 단어
    pronunciation = models.CharField(max_length=255, blank=True, null=True)  # 발음하는 법
    category = models.CharField(max_length=100, blank=True, null=True)  # 분류
    meaning = models.TextField()  # 단어의 의미

    def __str__(self):
        return self.word_text
