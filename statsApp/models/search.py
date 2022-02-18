from itertools import count
from django.db import models
from django.utils import timezone

class Search(models.Model):
    """Represents the data to persist about the searches in the frontend
    """
    id = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length = 120)
    count = models.IntegerField(default=1)
    start_date = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField(default=timezone.now)
    last_results = models.IntegerField()

    def update_current(self, last_results):
        self.count = self.count + 1
        self.last_date = timezone.now()
        self.last_results = last_results