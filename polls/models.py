from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    content = models.TextField()
    snippet = models.CharField(max_length=500)
    pubdate = models.DateTimeField()
    likes = models.PositiveIntegerField()

    def __unicode__(self):
        return self.title


class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    about = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    pass