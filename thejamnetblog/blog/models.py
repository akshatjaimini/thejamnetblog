from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=1000)
    category = models.CharField(max_length = 100,default="gen")
    date = models.DateField(_(u"Date"), blank = True)
    time = models.TimeField(_(u"Time"), blank=True)
    blog = models.TextField()