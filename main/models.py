from django.db import models
import datetime,time
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class FavoriteSubject(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    subject = models.CharField(max_length=40)
    reason = models.CharField(max_length=300)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.subject
    
