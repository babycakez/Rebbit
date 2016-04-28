import uuid

from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Sub_rebb(models.Model):
    sub_r = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s' % (self.sub_r)

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    creator = models.ForeignKey(Person)
    rpost = models.CharField(max_length=10000)
    firstlink = models.CharField(max_length=40,default="No Link Provided")
    secondlink = models.CharField(max_length=40,default="No Link Provided")
    thirdlink = models.CharField(max_length=40,default="No Link Provided")
    subreddit = models.ForeignKey(Sub_rebb)
    count = models.IntegerField(default=0)
    id = str(uuid.uuid4())

    def __unicode__(self):
        return u'%s %s' % (self.rpost, self.subreddit)

class Voting(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Person)
    votechoice = models.ForeignKey(Post)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Person)
    comment = models.CharField(max_length=1000)
    post = models.ForeignKey(Post)
    count = models.IntegerField(default=0)


class CommentVoting(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Person)
    votechoice = models.ForeignKey(Comment)