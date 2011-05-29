from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Record(models.Model):
    TYPE_CHOICES = (
        ("B", _("Book")),
    )
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=2048)
    helmet_record_id = models.CharField(max_length=16)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    
class BookShelf(models.Model):
    owner = models.ForeignKey(User)
    records = models.ManyToManyField(Record)