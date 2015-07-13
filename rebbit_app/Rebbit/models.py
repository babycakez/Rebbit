from django.db import models
import uuid
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    #birthday = models.DateField()

    #gender = models.IntegerField(choices=(
        #(1, "Male"),
        #(2, "Female"),
    #))

    email = models.EmailField()
    username = models.CharField(max_length=20)
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
    rpost = models.CharField(max_length=500)
    subreddit = models.ForeignKey(Sub_rebb)
    id = str(uuid.uuid4())

    def __unicode__(self):
        return u'%s' % (self.rpost)


