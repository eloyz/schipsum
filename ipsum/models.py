from django.db import models


class Phrase(models.Model):
    """Phrase that might be said in office through out day"""
    phrase = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    approved = models.BooleanField()

    def __unicode__(self):
        return self.phrase
