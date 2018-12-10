from django.db import models


class Question(models.Model):
    """
    Model for PDPs to submit their questions.
    """
    body = models.TextField(default='')
    votes = models.IntegerField(default=0)
    isAppropriate = models.BooleanField(default=False)
    isAnswered = models.BooleanField(default=False)
    timeStamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.body
