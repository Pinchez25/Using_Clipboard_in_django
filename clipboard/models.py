from django.db import models

class Quote(models.Model):
    quote = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.quote[:20])

