from itertools import count
from django.db import models
from django.utils import timezone

class Search(models.Model):

    id = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length = 120)
    count = models.IntegerField()
    start_date = models.DateTimeField()
    last_date = models.DateTimeField(default=timezone.now)
    last_results = models.IntegerField()