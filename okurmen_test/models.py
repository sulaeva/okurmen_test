from django.db import models

class Question(models.Model):
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
