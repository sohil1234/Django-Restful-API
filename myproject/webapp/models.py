from django.db import models

class student(models.Model):
    firstname= models.CharField(max_length=10)
    lastname= models.CharField(max_length=10)
    Age= models.IntegerField()
    Rollnumber= models.IntegerField()



    def __str__(self):
        return self.firstname


