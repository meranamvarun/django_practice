from django.db import models
from time import time 

# Create your models here.

def get_upload_file_name(instance,filename):
    return "useruploaded/%s_%s" %(str(time()).replace('.','_'),filename)    

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField()
    thumbnail = models.FileField(null=True,upload_to=get_upload_file_name)
    
    def __unicode__(self):
        return self.title

class comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    articles = models.ForeignKey(Article)
