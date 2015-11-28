from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Problem(models.Model):
    oj_id = models.IntegerField()

    @property
    def share_url(self):
        return reverse('problem:share', kwargs={'oj_id': self.oj_id})

    def get_absolute_url(self):
        return reverse('problem:problem', kwargs={'oj_id': self.oj_id})


class Code(models.Model):
    user = models.ForeignKey(User)
    problem = models.ForeignKey(Problem)
    text = models.TextField(default='')


class Hint(models.Model):
    user = models.ForeignKey(User)
    problem = models.ForeignKey(Problem)
    text = models.TextField()
